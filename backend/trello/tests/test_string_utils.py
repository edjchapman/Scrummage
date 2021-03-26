from django.test import TestCase

from trello.utils.string_utils import get_est


class GetEstimateUtilTests(TestCase):
    """
    Test the get_est util function.
    Make sure it extracts the correct values.
    """
    scenarios = [
        {
            "card_title": "(5.0) [2days likely] ADev implement stripe 3d secure verification for adding new cards",
            "expected_estimate": 5.0,
            "expected_consumed_extra": None
        },
        {
            "card_title": "(?) (Part of 2233) Keep state filtering for locations",
            "expected_estimate": None,
            "expected_consumed_extra": None
        },
        {
            "card_title": "(0) ADev re-write test for DELIVERY SLOTS the new factories.[0.5]",
            "expected_estimate": 0,
            "expected_consumed_extra": 0.5
        },
        {
            "card_title": "(?) ADev i can use the populate script without it throwing errors [5]",
            "expected_estimate": None,
            "expected_consumed_extra": 5.0
        },
    ]

    def test_regex_extracts_correct_estimate(self):
        for s in self.scenarios:
            self.assertEqual(
                get_est(s.get("card_title")),
                s.get("expected_estimate")
            )

    def test_regex_extracts_correct_consumed_extra(self):
        for s in self.scenarios:
            self.assertEqual(
                get_est(s.get("card_title"), bracket_style="[]"),
                s.get("expected_consumed_extra")
            )
