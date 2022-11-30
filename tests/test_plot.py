"""
Tests the module plot.py
"""
from unittest import TestCase

import matplotlib.pyplot as plt
from tdata import DATA_TIMESERIES, DATA_TITANIC

import devted.plot as dtplot


# Helper


SURVIVED = "Survived"
EMBARKED = "Embarked"
AGE = "Age"
CLASS = "Pclass"
FARE = "Fare"


DATE = "Date"
CLOSE = "Close"


DEFAULT_TITLE = "TITLE"
TEST_TITLE = "testTitle"
TEST_XLABEL = "testXLabel"
TEST_YLABEL = "testYLabel"
EXP_TITLE = "TESTTITLE"
EXP_XLABEL = "Testxlabel"
EXP_YLABEL = "Testylabel"


def check_title_and_labels(
    test_cls_ptr: TestCase,
    ax: plt.Axes,
    exp_title: str = EXP_TITLE,
    exp_xlabel: str = EXP_XLABEL,
    exp_ylabel: str = EXP_YLABEL,
) -> None:
    """Checks title and labels"""
    cls_name = test_cls_ptr.__class__.__name__
    err_msg = f"Class: {cls_name}"
    title = ax.get_title()
    xlabel = ax.get_xlabel()
    ylabel = ax.get_ylabel()

    test_cls_ptr.assertEqual(title, exp_title, err_msg)
    test_cls_ptr.assertEqual(xlabel, exp_xlabel, err_msg)
    test_cls_ptr.assertEqual(ylabel, exp_ylabel, err_msg)


# Tests


class TestHelper(TestCase):
    """Tests helper functions of _plot.py module"""

    def test_prep_labels(self):
        """Should capitalize labels, if given"""
        self.assertTrue(True)


class TestHistPlot(TestCase):
    """Tests histplot"""

    def setUp(self):
        plt.clf()
        self.X = AGE
        self.Y = None
        self.DATA = DATA_TITANIC

    def test_basic(self):
        """Tests the basic call with default params"""
        ax = dtplot.histplot(x=self.X, data=self.DATA)
        check_title_and_labels(
            self,
            ax,
            exp_xlabel=self.X,
            exp_ylabel="Count",
            exp_title=DEFAULT_TITLE
        )

    def test_basic_2(self):
        """Tests the basic call with kwargs"""
        ax = dtplot.histplot(
            x=self.X,
            data=self.DATA,
            title=TEST_TITLE,
            xlabel=TEST_XLABEL,
            ylabel=TEST_YLABEL,
        )
        check_title_and_labels(self, ax)

    def test_basic_3(self):
        """Tests the basic call with set_kwargs"""
        ax = dtplot.histplot(
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
    """Tests countplot"""

    def setUp(self):
        plt.clf()
        self.X = EMBARKED
        self.Y = None
        self.DATA = DATA_TITANIC

    def test_basic(self):
        """Tests the basic call with default params"""
        ax = dtplot.countplot(x=self.X, data=self.DATA)
        check_title_and_labels(
            self,
            ax,
            exp_xlabel=self.X,
            exp_ylabel="Count",
            exp_title=DEFAULT_TITLE
        )

    def test_basic_2(self):
        """Tests the basic call with kwargs"""
        ax = dtplot.countplot(
            x=self.X,
            data=self.DATA,
            title=TEST_TITLE,
            xlabel=TEST_XLABEL,
            ylabel=TEST_YLABEL,
        )
        check_title_and_labels(self, ax)

    def test_basic_3(self):
        """Tests the basic call with set_kwargs"""
        ax = dtplot.countplot(
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
    """Tests pointplot"""

    def setUp(self):
        plt.clf()
        self.X = CLASS
        self.Y = SURVIVED
        self.DATA = DATA_TITANIC

    def test_basic(self):
        """Tests the basic call with default params"""
        ax = dtplot.pointplot(x=self.X, y=self.Y, data=self.DATA)
        check_title_and_labels(
            self,
            ax,
            exp_xlabel=self.X,
            exp_ylabel=self.Y,
            exp_title=DEFAULT_TITLE
        )

    def test_basic_2(self):
        """Tests the basic call with kwargs"""
        ax = dtplot.pointplot(
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
        ax = dtplot.pointplot(
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


class TestScatterPlot(TestCase):
    """Tests scatterplot"""

    def setUp(self):
        plt.clf()
        self.X = CLASS
        self.Y = SURVIVED
        self.DATA = DATA_TITANIC

    def test_basic(self):
        """Tests the basic call with default params"""
        ax = dtplot.scatterplot(x=self.X, y=self.Y, data=self.DATA)
        check_title_and_labels(
            self,
            ax,
            exp_xlabel=self.X,
            exp_ylabel=self.Y,
            exp_title=DEFAULT_TITLE
        )

    def test_basic_2(self):
        """Tests the basic call with kwargs"""
        ax = dtplot.scatterplot(
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
        ax = dtplot.scatterplot(
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


class TestBarPlot(TestCase):
    """Tests barplot"""

    def setUp(self):
        plt.clf()
        self.X = EMBARKED
        self.Y = FARE
        self.DATA = DATA_TITANIC

    def test_basic(self):
        """Tests the basic call with default params"""
        ax = dtplot.barplot(x=self.X, y=self.Y, data=self.DATA)
        check_title_and_labels(
            self,
            ax,
            exp_xlabel=self.X,
            exp_ylabel=self.Y,
            exp_title=DEFAULT_TITLE
        )

    def test_basic_2(self):
        """Tests the basic call with kwargs"""
        ax = dtplot.barplot(
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
        ax = dtplot.barplot(
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


class TestLinePlot(TestCase):
    """Tests histplot"""

    def setUp(self):
        plt.clf()
        self.X = DATE
        self.Y = CLOSE
        self.DATA = DATA_TIMESERIES

    def test_basic(self):
        """Tests the basic call with default params"""
        ax = dtplot.lineplot(x=self.X, y=self.Y, data=self.DATA)
        check_title_and_labels(
            self,
            ax,
            exp_xlabel=self.X,
            exp_ylabel=self.Y,
            exp_title=DEFAULT_TITLE
        )

    def test_basic_2(self):
        """Tests the basic call with kwargs"""
        ax = dtplot.lineplot(
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
        ax = dtplot.lineplot(
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


class TestRegPlot(TestCase):
    """Tests histplot"""

    def setUp(self):
        plt.clf()
        self.X = CLOSE
        self.Y = CLOSE
        self.DATA = DATA_TIMESERIES

    def test_basic(self):
        """Tests the basic call with default params"""
        ax = dtplot.regplot(x=self.X, y=self.Y, data=self.DATA)
        check_title_and_labels(
            self,
            ax,
            exp_xlabel=self.X,
            exp_ylabel=self.Y,
            exp_title=DEFAULT_TITLE
        )

    def test_basic_2(self):
        """Tests the basic call with kwargs"""
        ax = dtplot.regplot(
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
        ax = dtplot.regplot(
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


class TestKdePlot(TestCase):
    """Tests kdeplot"""

    def setUp(self):
        plt.clf()
        self.X = AGE
        self.DATA = DATA_TITANIC

    def test_basic(self):
        """Tests the basic call with default params"""
        ax = dtplot.kdeplot(x=self.X, data=self.DATA)
        check_title_and_labels(
            self,
            ax,
            exp_xlabel=self.X,
            exp_ylabel="Density",
            exp_title=DEFAULT_TITLE
        )

    def test_basic_2(self):
        """Tests the basic call with kwargs"""
        ax = dtplot.kdeplot(
            x=self.X,
            data=self.DATA,
            title=TEST_TITLE,
            xlabel=TEST_XLABEL,
            ylabel=TEST_YLABEL,
        )
        check_title_and_labels(self, ax)

    def test_basic_3(self):
        """Tests the basic call with set_kwargs"""
        ax = dtplot.kdeplot(
            x=self.X,
            data=self.DATA,
            set_kwargs={
                "title": TEST_TITLE,
                "xlabel": TEST_XLABEL,
                "ylabel": TEST_YLABEL
            }
        )
        check_title_and_labels(self, ax)
