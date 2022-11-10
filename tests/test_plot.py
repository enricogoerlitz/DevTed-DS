"""
Tests the functions of the _plot.py module
"""
import devted as dt
import matplotlib.pyplot as plt
import pandas as pd

from unittest import TestCase


df = pd.read_csv("../data/titanic_data.csv")
SURVIVED = "Survived"
EMBARKED = "Embarked"
AGE = "Age"
CLASS = "Pclass"


def check_title_and_labels(
    test_cls_ptr: TestCase,
    ax: plt.Axes,
    exp_title: str,
    exp_xlabel: str,
    exp_ylabel: str
) -> None:
    """Checks title and labels"""
    title = ax.get_title()
    xlabel = ax.get_xlabel()
    ylabel = ax.get_ylabel()

    test_cls_ptr.assertEqual(title, exp_title)
    test_cls_ptr.assertEqual(xlabel, exp_xlabel)
    test_cls_ptr.assertEqual(ylabel, exp_ylabel)



class TestHelper(TestCase):
    """Tests helper functions of _plot.py module"""

    def test_prep_labels(self):
        """Should capitalize labels, if given"""
        self.assertTrue(True)


class TestHistPlot(TestCase):
    """Tests histplot"""

    def test_basic(self):
        """Tests the basic call"""
        expected_title = "TITLE"
        expected_xlabel = AGE
        expected_ylabel = "Count"
        ax = dt.histplot(x=AGE, data=df)
        check_title_and_labels(
            self,
            ax,
            expected_title,
            expected_xlabel,
            expected_ylabel
        )
