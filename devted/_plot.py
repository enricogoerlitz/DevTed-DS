"""
DevTed plots for better handling the seaborn plots.
Brings intellisense with the most used params.
"""
import seaborn as sns
import matplotlib.pyplot as plt

from typing import Literal, Callable, Union

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
    xlabel: Union[str, None] = None,
    ylabel: Union[str, None] = None,
    bins: Union[str, int, Vector] = "auto",
    hue: Union[str, None] = None,
    kde: bool = False,
    ax: Union[plt.Axes, None] = None,
    set_kwargs: dict = None,
    cumulative: bool = False,
    kde_kws: Union[dict, None] = None,
    zip_params: dict
) -> plt.Axes:
    if not xlabel: xlabel = x
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
    data: Union[PandasObject, None] = None,
    title: str = "TITLE",
    xlabel: Union[str, None] = None,
    ylabel: Union[str, None] = None,
    hue: Union[str, None] = None,
    hue_order: Union[Vector, None] = None,
    order: Union[Vector, None] = None,
    orient: Literal["h", "v"] = "v",
    set_kwargs: dict = None,
    ax: Union[plt.Axes, None] = None,
    zip_params: dict
) -> plt.Axes:
    if orient == "h":
        if not ylabel: ylabel = x
        if not xlabel: xlabel = "Count"
        zip_params["y"] = zip_params["x"]
        del zip_params["x"]
    else:
        if not xlabel: xlabel = x
        if not ylabel: ylabel = "Count"

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
    x: Union[str, None] = None,
    y: Union[str, None] = None,
    hue: Union[str, None] = None,
    data: Union[PandasObject, None] = None,
    title: str = "TITLE",
    xlabel: Union[str, None] = None,
    ylabel: Union[str, None] = None,
    order: Union[Vector, None] = None,
    hue_order: Union[Vector, None] = None,
    ci: int = 95,
    errorbar: Literal["ci", "pi", "se", "sd"] = "ci",
    markers: Marker = "o",
    linestyles: LineStyle = "-",
    ax: Union[plt.Axes, None] = None,
    set_kwargs: dict = None,
    zip_params: dict
) -> plt.Axes:
    if not xlabel: xlabel = x
    if not ylabel: ylabel = y
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


@zipparams(ignore=BASE.split())
def scatterplot(
    *,
    x: str = None,
    y: str = None,
    data: DataFrame = None,
    title: str = "TITLE",
    xlabel: Union[str, None] = None,
    ylabel: Union[str, None] = None,
    hue: Union[str, None] = None,
    alpha: Union[float, None] = None,
    ax: Union[plt.Axes, None] = None,
    set_kwargs: dict = None,
    zip_params: dict
) -> plt.Axes:
    if not xlabel: xlabel = x
    if not ylabel: ylabel = y
    set_kwargs = _prep_set_kwargs(
        title,
        xlabel,
        ylabel,
        set_kwargs
    )
    return _plot(
        sns.scatterplot,
        zip_params,
        set_kwargs
    )


@zipparams(ignore=BASE.split())
def barplot(
    *,
    x: str = None,
    y: str = None,
    data: DataFrame = None,
    title: str = "TITLE",
    xlabel: Union[str, None] = None,
    ylabel: Union[str, None] = None,
    order: Union[Vector, None] = None,
    hue: Union[str, None] = None,
    hue_order: Union[Vector, None] = None,
    ci: Union[int, None] = None,
    orient: Literal["h", "v"] = "v",
    ax: Union[plt.Axes, None] = None,
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
        sns.barplot,
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
    xlabel: Union[str, None],
    ylabel: Union[str, None],
    set_kwargs: Union[dict, None]
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
