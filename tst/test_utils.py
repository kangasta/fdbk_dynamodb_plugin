import os
from decimal import Decimal
from unittest import TestCase

from fdbk_dynamodb_plugin.utils import obj_decimals_to_numbers


class UtilsTest(TestCase):
    def test_obj_decimals_to_numbers(self):
        before = dict(f=Decimal(1.5), i=Decimal(3))
        after = obj_decimals_to_numbers(before)

        self.assertAlmostEqual(after.get('f'), 1.5)
        self.assertEqual(after.get('i'), 3)
