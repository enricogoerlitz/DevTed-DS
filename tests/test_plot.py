"""
Tests the functions of the _plot.py module
"""
import devted as dt
import matplotlib.pyplot as plt
import pandas as pd

from unittest import TestCase


# Data


df = pd.read_csv("titanic_data.csv")
SURVIVED = "Survived"
EMBARKED = "Embarked"
AGE = "Age"
CLASS = "Pclass"


# Helper constants

TEST_TITLE = "testTitle"
TEST_XLABEL = "testXLabel"
TEST_YLABEL = "testYLabel"
EXP_TITLE = "TestTitle"
EXP_XLABEL = "TestXLabel"
EXP_YLABEL = "TestYLabel"


def check_title_and_labels(
    test_cls_ptr: TestCase,
    ax: plt.Axes,
    exp_title: str = EXP_TITLE,
    exp_xlabel: str = EXP_XLABEL,
    exp_ylabel: str = EXP_YLABEL
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

    def setUp(self):
        self.X = AGE
        self.Y = None
        self.DATA = df

    def test_basic(self):
        """Tests the basic call with default params"""
        ax = dt.histplot(x=self.X, data=self.DATA)
        check_title_and_labels(self, ax)

    def test_basic_2(self):
        """Tests the basic call with kwargs"""
        ax = dt.histplot(
            x=self.X,
            data=self.DATA,
            title=TEST_TITLE,
            xlabel=TEST_XLABEL,
            ylabel=TEST_YLABEL,
        )
        check_title_and_labels(self, ax)

    def test_basic_3(self):
        """Tests the basic call with set_kwargs"""
        ax = dt.histplot(
            x=self.X,
            data=self.DATA,
            set_kwargs={
                "title": TEST_TITLE,
                "xlabel": TEST_XLABEL,
                "ylabel": TEST_YLABEL
            }
        )
        check_title_and_labels(self, ax)


class TestCountPlot(TestCase):
    """Tests histplot"""

    def setUp(self):
        self.X = EMBARKED
        self.Y = None
        self.DATA = df

    def test_basic(self):
        """Tests the basic call with default params"""
        ax = dt.countplot(x=self.X, data=self.DATA)
        check_title_and_labels(self, ax)

    def test_basic_2(self):
        """Tests the basic call with kwargs"""
        ax = dt.countplot(
            x=self.X,
            y=self.Y,
            data=self.DATA,
            title=TEST_TITLE,
            xlabel=TEST_XLABEL,
            ylabel=TEST_YLABEL,
        )
        check_title_and_labels(self, ax)

    def test_basic_3(self):
        """Tests the basic call with set_kwargs"""
        ax = dt.countplot(
            x=self.X,
            data=self.DATA,
            set_kwargs={
                "title": TEST_TITLE,
                "xlabel": TEST_XLABEL,
                "ylabel": TEST_YLABEL
            }
        )
        check_title_and_labels(self, ax)


class TestPointPlot(TestCase):
    """Tests histplot"""

    def setUp(self):
        self.X = CLASS
        self.Y = SURVIVED
        self.DATA = df

    def test_basic(self):
        """Tests the basic call with default params"""
        ax = dt.pointplot(x=self.X, data=self.DATA)
        check_title_and_labels(self, ax)

    def test_basic_2(self):
        """Tests the basic call with kwargs"""
        ax = dt.pointplot(
            x=self.X,
            y=self.Y,
            data=self.DATA,
            title=TEST_TITLE,
            xlabel=TEST_XLABEL,
            ylabel=TEST_YLABEL,
        )
        check_title_and_labels(self, ax)

    def test_basic_3(self):
        """Tests the basic call with set_kwargs"""
        ax = dt.pointplot(
            x=self.X,
            y=self.Y,
            data=self.DATA,
            set_kwargs={
                "title": TEST_TITLE,
                "xlabel": TEST_XLABEL,
                "ylabel": TEST_YLABEL
            }
        )
        check_title_and_labels(self, ax)
