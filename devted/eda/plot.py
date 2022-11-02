"""
EDA prep plots...
"""
from typing import Any

import seaborn as sns


def histplot(
    data: Any | None = None,
    *,
    x: Any | None = None,
    y: Any | None = None,
    hue: Any | None = None,
    title: str = "Title",
    weights: Any | None = None,
    stat: str = "count",
    bins: str = "auto",
    binwidth: Any | None = None,
    binrange: Any | None = None, 
    discrete: Any | None = None, 
    cumulative: bool = False, 
    common_bins: bool = True, 
    common_norm: bool = True, 
    multiple: str = "layer", 
    element: str = "bars", 
    fill: bool = True, 
    shrink: int = 1, 
    kde: bool = False, 
    kde_kws: Any | None = None, 
    line_kws: Any | None = None, 
    thresh: int = 0, 
    pthresh: Any | None = None, 
    pmax: Any | None = None, 
    cbar: bool = False, 
    cbar_ax: Any | None = None, 
    cbar_kws: Any | None = None, 
    palette: Any | None = None, 
    hue_order: Any | None = None, 
    hue_norm: Any | None = None, 
    color: Any | None = None, 
    legend: bool = True, 
    ax: Any | None = None, 
    **kwargs: Any
) -> Any:
    return None