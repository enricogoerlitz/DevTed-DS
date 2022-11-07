"""
Custom DevTed typing collections
"""
from pandas import Series, DataFrame


Vector = list | tuple | Series
PandasObject = Series | DataFrame
