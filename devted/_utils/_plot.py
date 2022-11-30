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
