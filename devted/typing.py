"""
Custom DevTed typing collections
"""
from typing import Literal
from pandas import Series, DataFrame


Vector = list | tuple | Series
PandasObject = Series | DataFrame
LineStyle = Literal["-", "--", ":"]
Marker = Literal[
    ".", "o", "8", "s",
    "p", "P", "*", "h",
    "H", "+", "x", "d",
    "D", "|", "_", ""
]
