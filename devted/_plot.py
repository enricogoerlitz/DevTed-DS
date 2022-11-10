"""
DevTed plots for better handling the seaborn plots.
Brings intellisense with the most used params.
"""
import seaborn as sns
import matplotlib.pyplot as plt

from typing import Literal, Callable

from .typing import Vector, Marker, LineStyle, PandasObject
from ._decorators import zipparams

from pandas import Series, DataFrame

BASE = "title xlabel ylabel set_kwargs"
ORIENT = f"{BASE} orient"

@zipparams(ignore=BASE.split())
def histplot(
    *,
    x: str = None,
    data: DataFrame = None,
    title: str = "TITLE",
    xlabel: str | None = None,
    ylabel: str | None = None,
    bins: str | int | Vector = "auto",
    hue: str | None = None,
    kde: bool = False,
    ax: plt.Axes | None = None,
    set_kwargs: dict = None,
    cumulative: bool = False,
    kde_kws: dict | None = None,
    zip_params: dict
) -> plt.Axes:
    set_kwargs = _prep_set_kwargs(
        title,
        xlabel,
        ylabel,
        set_kwargs
    )
    return _plot(
        sns.histplot,
        zip_params,
        set_kwargs
    )


@zipparams(ignore=ORIENT.split())
def countplot(
    *, 
    x: str = None,
    data: PandasObject | None = None,
    title: str = "TITLE",
    xlabel: str | None = None,
    ylabel: str | None = None,
    hue: str | None = None,
    hue_order: Vector | None = None,
    order: Vector | None = None,
    orient: Literal["h", "v"] = "v",
    set_kwargs: dict = None,
    ax: plt.Axes | None = None,
    zip_params: dict
) -> plt.Axes:
    if orient == "h":
        zip_params["y"] = zip_params["x"]
        del zip_params["x"]
    set_kwargs = _prep_set_kwargs(
        title,
        xlabel,
        ylabel,
        set_kwargs
    )
    return _plot(
        sns.countplot,
        zip_params,
        set_kwargs
    )


@zipparams(ignore=BASE.split())
def pointplot(
    *,
    x: str | None = None,
    y: str | None = None,
    hue: str | None = None,
    data: PandasObject | None = None,
    title: str = "TITLE",
    xlabel: str | None = None,
    ylabel: str | None = None,
    order: Vector | None = None,
    hue_order: Vector | None = None,
    ci: int = 95,
    errorbar: Literal["ci", "pi", "se", "sd"] = "ci",
    markers: Marker = "o",
    linestyles: LineStyle = "-",
    ax: plt.Axes | None = None,
    set_kwargs: dict = None,
    zip_params: dict
) -> plt.Axes:
    set_kwargs = _prep_set_kwargs(
        title,
        xlabel,
        ylabel,
        set_kwargs
    )
    return _plot(
        sns.pointplot,
        zip_params,
        set_kwargs
    )


# Private Helper-Functions


def _plot(
    plot_func: Callable,
    plot_kwargs: dict,
    set_kwargs
) -> plt.Axes:
    ax = plot_func(**plot_kwargs)
    ax.set(**set_kwargs)
    return ax


def _prep_set_kwargs(
    title: str, 
    xlabel: str | None,
    ylabel: str | None,
    set_kwargs: dict | None
) -> dict:
    set_kwargs = (
        {"title": title} | 
        ({} if not xlabel else {"xlabel": xlabel}) |
        ({} if not ylabel else {"ylabel": ylabel}) |
        ({} if not isinstance(set_kwargs, dict) else set_kwargs)
    )
    set_kwargs = _prep_title(set_kwargs)
    set_kwargs = _prep_labels(set_kwargs)
    return set_kwargs


def _prep_title(kwargs: dict) -> dict:
    kwargs["title"] = kwargs.get("title", "TITLE").upper()
    return kwargs


def _prep_labels(kwargs: dict) -> dict:
    xlabel: str = kwargs.get("xlabel", None)
    ylabel: str = kwargs.get("ylabel", None)
    if xlabel:
        kwargs["xlabel"] = xlabel.capitalize()
    if ylabel:
        kwargs["ylabel"] = ylabel.capitalize()
    return kwargs
