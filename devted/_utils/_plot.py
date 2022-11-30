"""
Utils functions for plots
Will be imported from the plot module
"""
import os
import shutil  # noqa
import uuid
import matplotlib.pyplot as plt

from glob import glob
from typing import Literal
from ._utils import zero_prefix
from matplotlib.ticker import MaxNLocator
from pandas import DataFrame


def axis_to_int(ax: plt.Axes, axis: Literal["x", "y"]) -> None:
    """Sets the x or y axis numbers from floats to integers"""
    if axis == "x":
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    elif axis == "y":
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))


def export_plot(notebook_name="notebook1", plot_name="") -> str:
    dirpath = _get_plot_dirpath(notebook_name)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    plotname = _get_fig_title_as_filename(dirpath, plot_name)
    full_plot_path = os.path.join(dirpath, plotname)

    plt.savefig(full_plot_path)


def clear_plots_dir(notebook_name="notebook1") -> None:
    dirpath = _get_plot_dirpath(notebook_name)
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)


class DataFramePlotter:
    """
    intern entscheiden, ob plot_target_relation/_cat!
    """

    def __init__(
        self,
        df: DataFrame,
        target_column: str
    ) -> None:
        self.df = df
        self.target_column = target_column

    def target_relation(column: str) -> plt.Axes:
        pass

    def distribution(column: str) -> plt.Axes:
        pass

    def _target_relation_num(column: str) -> plt.Axes:
        pass

    def _target_relation_cat(column: str) -> plt.Axes:
        pass

    def _distribution_num(column: str) -> plt.Axes:
        pass

    def _distribution_cat(column: str) -> plt.Axes:
        pass


# def plot_target_relation(column_name):
#     _, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
#     ax1, ax2 = axes

#     target_pvt = df.pivot_table(index=column_name, values=TARGET, aggfunc="mean").sort_index()  # noqa

#     sns.pointplot(x=TARGET, y=column_name, data=df, ax=ax1).set_title(f"Relation Hazardous and {column_name}")  # noqa
#     sns.regplot(x=target_pvt.index, y=target_pvt.to_numpy(), ci=False, line_kws={"color": "C1"}, scatter_kws={"alpha": 0.5}, ax=ax2).set_title(f"Linear Relation Hazardous and {column_name}")  # noqa


# def plot_target_relation_cat(column_name):
#     g = sns.pointplot(x=column_name, y=TARGET, data=df)
#     g.set_title(f"Relation Hazardous-Mean and {column_name}")
#     g.tick_params(axis='x', rotation=45)


# def plot_dist(column_name):
#     _, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
#     ax1, ax2 = axes
    
#     title = f"Distribution of {column_name}"
#     ax1.set_title(title)
#     ax2.set_title(title)

#     sns.boxplot(x=column_name, data=df, ax=ax1)
#     df[column_name].hist(ax=ax2)

#     print(f"Skew: \t {df[column_name].skew()}")


# def plot_dist_cat(column_name):
#     g = sns.countplot(x=column_name, data=df, color="C0")
#     g.tick_params(axis='x', rotation=45)
#     g.set_title(f"Distribution of {column_name}")


# Private Helper-Functions


def _get_plot_dirpath(notebook_name="notebook1") -> str:
    return os.path.join(os.getcwd(), "plots", notebook_name)


def _get_fig_title_as_filename(dirpath: str, plot_name: str) -> str:
    """
    Returns the figure title and a number prefix
    """
    try:
        plot_count = len(glob(os.path.join(dirpath, "*.jpg"))) + 1
        count_prefix = zero_prefix(plot_count)

        if plot_name.strip():
            plotname = plot_name.replace(" ", "_").lower()
            return f"{count_prefix}_{plotname}"

        plotname = plt.gcf().axes[0].get_title()
        if plotname.strip():
            plotname: str = plotname.replace(" ", "_").lower()
            return f"{count_prefix}_{plotname}.jpg"

        return f"{count_prefix}_{uuid.uuid1().hex}.jpg"
    except Exception:
        default_filename: str = f"{uuid.uuid1().hex}.jpg"
        return default_filename
