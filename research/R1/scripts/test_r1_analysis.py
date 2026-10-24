"""Deterministic tests for the R1 offline evidence and missingness rules."""
import math
import tempfile
import unittest
from pathlib import Path
from r1_analysis import (
    HERE, LENSES, anchor_rows, break_diagnostics, finite_positive, fit_rss,
    month_quarter, offline, read_anchor_observations, read_anchor_prices, read_csv
)


class FrozenR1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obs = read_anchor_observations(HERE / "exhibits/observations-q1.csv")
        cls.prices = read_anchor_prices(HERE / "exhibits/price-checkpoints-q1.csv")
        cls.rows = anchor_rows(cls.obs, cls.prices)

    def lookup(self, year, lens):
        return next(row for row in self.rows
                    if row["start"] == str(year) + "Q1"
                    and row["compensation_lens"] == lens)

    def test_frozen_csv_exact_reproduction(self):
        frozen = read_csv(HERE / "exhibits/sensitivity-q1.csv")
        self.assertEqual(self.rows, frozen)

    def test_offline_cli_core(self):
        with tempfile.TemporaryDirectory() as folder:
            offline(Path(folder))
            output = read_csv(Path(folder) / "sensitivity-q1-reproduced.csv")
            self.assertEqual(output, self.rows)

    def test_anchor_revisions_are_preserved(self):
        self.assertEqual(self.obs[1973]["OPHNFB"], 46.272)
        self.assertEqual(self.obs[2025]["COMPNFB"], 143.108)
        self.assertEqual(self.obs[2025]["COMPRNFB"], 109.465)

    def test_published_real_vs_output_price_are_distinct(self):
        a = self.lookup(1973, LENSES[0])
        b = self.lookup(1973, LENSES[1])
        self.assertAlmostEqual(float(a["compensation_growth_pct"]), 62.26653, places=4)
        self.assertAlmostEqual(float(b["compensation_growth_pct"]), 120.82547, places=4)
        self.assertNotEqual(a["compensation_growth_pct"], b["compensation_growth_pct"])

    def test_raw_cpi_not_mislabeled_bls_real_comp(self):
        r = self.lookup(1973, LENSES[0])
        c = self.lookup(1973, LENSES[3])
        self.assertAlmostEqual(float(c["compensation_growth_pct"]), 48.60215, places=4)
        self.assertNotEqual(r["compensation_growth_pct"], c["compensation_growth_pct"])

    def test_pce_is_available_only_when_frozen(self):
        self.assertAlmostEqual(
            float(self.lookup(1973, LENSES[2])["compensation_growth_pct"]),
            91.54608, places=4)
        self.assertFalse(any(row["start"] == "2000Q1" and row["compensation_lens"] == LENSES[2]
                             for row in self.rows))

    def test_monthly_quarter_requires_all_three_months(self):
        q = {"2025-07-01": 100.0, "2025-08-01": 103.0, "2025-09-01": 109.0}
        self.assertEqual(month_quarter(q, 2025, 3), 104.0)
        self.assertIsNone(month_quarter(q, 2025, 4))
        q.update({"2025-11-01": 110.0, "2025-12-01": 111.0})
        self.assertIsNone(month_quarter(q, 2025, 4))  # Oct 2025 is not estimated

    def test_bad_values_rejected(self):
        for value in ("0", "-1", "nan", "inf"):
            with self.assertRaises(ValueError):
                finite_positive(value)

    def test_bic_scans_nonpreselected_candidates(self):
        # Synthetic log-ratio has a 2005 slope change, not a 1973 presumption.
        x = {year: (0.003 * (year - 1960)
                    + 0.023 * max(0, year - 2005)
                    + 0.0003 * math.sin(year))
             for year in range(1960, 2026)}
        results = break_diagnostics(x, min_years=10)
        self.assertTrue(results)
        self.assertIn(2005, [r["candidate_year"] for r in results])
        self.assertLessEqual(abs(results[0]["candidate_year"] - 2005), 1)
        self.assertNotEqual(results[0]["candidate_year"], 1973)
        self.assertGreater(results[0]["bic_improvement"], 0)
        self.assertEqual(len(results), len(set(r["candidate_year"] for r in results)))

    def test_singular_matrix_and_insufficient_sample(self):
        with self.assertRaises(ValueError):
            fit_rss([[1.0, 1.0], [1.0, 1.0]], [1.0, 1.0])
        self.assertEqual(break_diagnostics({2001: 1.0, 2002: 2.0}), [])


if __name__ == "__main__":
    unittest.main()
