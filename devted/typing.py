"""
Custom DevTed typing collections
"""
from typing import Literal, Union
from pandas import Series, DataFrame


Vector = Union[list, tuple, Series]
PandasObject = Union[Series, DataFrame]
LineStyle = Literal["-", "--", ":"]
Marker = Literal[
    ".", "o", "8", "s",
    "p", "P", "*", "h",
    "H", "+", "x", "d",
    "D", "|", "_", ""
]
