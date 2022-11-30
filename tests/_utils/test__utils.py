"""
Tests the module _utils (general utils)
"""
import sys
import devted as dt

from io import StringIO
from typing import Any
from unittest import TestCase
from pandas import DataFrame


# Helper


def msg_not_eq(expected_value: Any, actual_value: Any) -> str:
    return f"\nExpected:\t{expected_value}\nActual\t\t{actual_value}"


# Tests


class TestZeroPrefix(TestCase):
    """Tests the function zero_prefix"""

    def test_smaller_then_ten(self):
        """
        Tests all numbers between 0 and 9
        The function should return these numbers with an 0 prefix
        like "0" -> "00" or "8" -> "08"
        """
        expeted_strings_tpl = [(i, f"0{i}") for i in range(0, 10)]
        for num, expected_str in expeted_strings_tpl:
            actual_str = dt.zero_prefix(num)
            self.assertEqual(
                actual_str,
                expected_str,
                msg_not_eq(expected_str, actual_str)
            )

    def test_grater_or_euqual_then_ten(self):
        """
        Tests 10 numbers grater or equal ten.
        It should just return the number as string.
        """
        expeted_strings_tpl = [(i, str(i)) for i in range(10, 21)]
        for num, expected_str in expeted_strings_tpl:
            actual_str = dt.zero_prefix(num)
            self.assertTrue(isinstance(actual_str, str), "Not a string")
            self.assertEqual(
                actual_str,
                expected_str,
                msg_not_eq(expected_str, actual_str)
            )


class TestHrStr(TestCase):
    """Tests function hrstr"""

    def test_basic(self):
        """
        Tests the basic call of the function.
        Should return a hour format like "08:15h"
        """
        value_expected_res = [
            (59.50, "00:59h"),
            (121.25, "02:01h"),
            (605.75, "10:05h"),
            (71.05, "01:11h"),
            (71.10, "01:11h")
        ]
        for minutes, expected_str in value_expected_res:
            actual_str = dt.hrstr(minutes)
            self.assertEqual(
                expected_str,
                actual_str,
                msg_not_eq(expected_str, actual_str)
            )

    def test_with_milliseconds(self):
        """
        Tests the function with milliseconds.
        Should return a hour format like "08:15:30h"
        """
        value_expected_res = [
            (59.50, "00:59:30h"),
            (121.25, "02:01:15h"),
            (605.75, "10:05:45h"),
            (71.05, "01:11:03h"),
            (71.10, "01:11:06h")
        ]
        for minutes, expected_str in value_expected_res:
            actual_str = dt.hrstr(minutes, milliseconds=True)
            self.assertEqual(
                expected_str,
                actual_str,
                msg_not_eq(expected_str, actual_str)
            )

    def test_with_none_suffix(self):
        """
        Tests the function without an suffix.
        Should return a hour format like "08:15:30".
        """
        expected_str_1 = "00:59"
        actual_str_1 = dt.hrstr(59.5, suffix=None)
        expected_str_2 = "00:59:30"
        actual_str_2 = dt.hrstr(59.5, suffix=None, milliseconds=True)
        self.assertEqual(
            expected_str_1,
            actual_str_1,
            msg_not_eq(expected_str_1, actual_str_1)
        )
        self.assertEqual(
            expected_str_2,
            actual_str_2,
            msg_not_eq(expected_str_2, actual_str_2)
        )


class TestPrintDfColumnsForConstants(TestCase):
    """
    Tests the function print_df_columns_for_constants
    """
    def setUp(self):
        self.expections = [
            'DFC_COLUMN_1 = "column 1"',
            'DFC_COLUMN_2 = "column-2"',
            'DFC_COLUMN_3 = "column_3"',
            'DFC_COLUMN_4 = "column.*+#4,;<>?!§$%&/()=?"',  # noqa
            'DFC_COLUMN_NAME_MY_BEAUTY_5 = "columnNameMyBeauty**5"',  # noqa
        ]
        self.df = DataFrame({
            "column 1": [1],
            "column-2": [1],
            "column_3": [1],
            "column.*+#4,;<>?!§$%&/()=?": [1],
            "columnNameMyBeauty**5": [1],
        })

    def test_basic(self):
        """
        Should print all df columns
        """
        console_out = StringIO()
        sys.stdout = console_out

        dt.print_df_columns_for_constants(self.df)

        output_lines = console_out.getvalue().split("\n")

        for i in range(0, len(self.expections)):
            expected_value = self.expections[i]
            actual_value = output_lines[i]
            self.assertEqual(
                expected_value,
                actual_value,
                msg_not_eq(actual_value, expected_value)
            )
