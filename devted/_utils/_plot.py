"""
Utils functions for plots
"""
import os
import os
import shutil
import uuid

from glob import glob
from typing import Literal
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator



def axis_to_int(ax: plt.Axes, axis: Literal["x", "y"]) -> None:
    if axis == "x":
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    elif axis == "y":
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))


def export_plot(notebook_name="notebook1", plot_name="") -> str:
    dirpath = get_plot_dirpath(notebook_name)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    plotname = get_fig_title(dirpath, plot_name)
    full_plot_path = os.path.join(dirpath, plotname)

    plt.savefig(full_plot_path)