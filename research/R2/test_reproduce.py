"""Regression checks for R2 arithmetic and provenance, stdlib-only."""
import unittest
import reproduce
from decimal import Decimal as D


class R2Model(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obs, cls.cases = reproduce.inputs()
        cls.sc = {r["id"]: reproduce.scenario(r) for r in cls.cases}

    def test_primary_sources_and_rates(self):
        self.assertEqual(self.obs["acs_hh_income_2024"], D(81604))
        self.assertEqual(self.obs["kff_worker_family_2026"], D(7471))
        self.assertEqual(len(self.sc), 5)

    def test_mortgage_index_population_mismatch_flag_not_removed(self):
        self.assertTrue(D(3) < self.obs["new_home_q1_1984"]/self.obs["cps_income_1984"] < D(4))
        self.assertTrue(D(4) < self.obs["new_home_q1_2025"]/self.obs["cps_income_2025"] < D(6))
        self.assertIn("Not same buyers", reproduce.render())

    def test_composition_matters_at_equal_gross_wages(self):
        self.assertEqual(self.sc["dual_100k"]["gross"], self.sc["one_100k"]["gross"])
        self.assertLess(self.sc["dual_100k"]["margin"], self.sc["one_100k"]["margin"])
        self.assertGreater(self.sc["dual_low_cost"]["margin"], self.sc["dual_high_cost"]["margin"])

    def test_shock_monotonic_and_zero(self):
        for r in self.sc.values():
            self.assertEqual(reproduce.shock_shortfall(r, 0), D(0))
            self.assertLessEqual(reproduce.shock_shortfall(r, 6000),
                                 reproduce.shock_shortfall(r, 15000))
            self.assertGreaterEqual(reproduce.lost_earner_shortfall(r, "first"), D(0))
        self.assertEqual(self.sc["one_60k"]["second"], D(0))

    def test_matched_renter_burden_counts(self):
        us = self.obs
        base = us["acs_rent_total_us_2024"] - us["acs_rent_notcomputed_us_2024"]
        cost = sum(us["acs_rent_" + key + "_us_2024"] for key in ("30_34", "35_39", "40_49", "50plus"))
        self.assertEqual(base, D(42954477))
        self.assertEqual(cost, D(22237262))
        self.assertEqual((cost / base * 100).quantize(D("0.1")), D("51.8"))
        self.assertIn("Washington state", reproduce.render())

    def test_real_income_deflator_vintage(self):
        self.assertEqual(self.obs["cps_real_income_1984"], D(61910))
        self.assertEqual(self.obs["cps_real_income_2025"], D(87460))
        self.assertIn("Not size-adjusted", reproduce.render())

    def test_display_and_frozen_format(self):
        self.assertEqual(reproduce.usd(D("-2000")), "-$2,000")
        self.assertEqual(reproduce.pp(D("-0.4")), "-0.4 pp")
        self.assertEqual(reproduce.render(), reproduce.render())
        self.assertIn("# R2 reproducible exhibits", reproduce.render())


if __name__ == "__main__":
    unittest.main()
