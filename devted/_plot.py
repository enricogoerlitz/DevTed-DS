"""
DevTed plots
"""
from ._typing import Vector
from ._decorators import zipparams

import seaborn as sns
import matplotlib.pyplot as plt

from typing import Any, Literal
from pandas import Series, DataFrame


@zipparams(ignore="title xlabel ylabel set_kws".split())
def histplot(
    *,
    x: str = None,
    data: DataFrame = None,
    title: str = "TITLE",
    xlabel: str | None = None,
    ylabel: str | None = None,
    bins: str | int | Vector = "auto",
    hue: Any | None = None,
    kde: bool = False,
    palette: Any | None = None,
    color: Any | None = None,
    legend: bool = True,
    ax: Any | None = None,
    set_kws: dict = None,
    cumulative: bool = False,
    multiple: Literal["layer", "dodge", "stack", "fill"] = "layer",
    element: Literal["bars", "step", "poly"] = "bars",
    fill: bool = True,
    kde_kws: Any | None = None,
    zip_params: dict = None,
    **kwargs: Any
) -> plt.Axes:
    set_kwargs = (
        {"title": title} | 
        ({} if not xlabel else {"xlabel": xlabel}) |
        ({} if not ylabel else {"ylabel": ylabel}) |
        ({} if not isinstance(set_kws, dict) else set_kws)
    )

    set_kwargs = _prep_title(set_kwargs)
    set_kwargs = _prep_labels(set_kwargs)
    
    ax = sns.histplot(**zip_params)
    ax.set(**set_kwargs)
    return ax


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
    
