"""
General utils
Will be imported from the devted module (main module)
"""
import devted.const as dtconst

from typing import Union
from devted.typing import Numeric
from pandas import DataFrame


def to_category(
    df: DataFrame,
    *,
    column: str,
    category_order: list
) -> DataFrame:
    """
    Convertes the dtype of an column in a ordered cateory.
    """
    return df[column].astype(dtconst.CATEGORY).cat.reorder_categories(category_order, ordered=True)  # noqa


def zero_prefix(number: Union[str, Numeric]) -> str:
    """
    Adds a 0 in front of a number between 0 and 9.
    If the number is 10 or higher, just the number will returned as string.
    """
    return f"0{number}" if int(number) < 10 else f"{number}"


def hrstr(
    minutes: Numeric,
    *,
    suffix: str = "h",
    milliseconds: bool = False
) -> str:
    """
    Tranformed minutes into an hour string like "15:05h" or
    if milliseconds equals True a hour string like "15:05:30h".
    You can also change the suffix from "h" to None or
    an other string you want.
    """
    suffix = suffix if suffix else ""
    hour_str = zero_prefix(int(minutes / dtconst.HOUR_MINUTES))
    min_str = zero_prefix(int(minutes % dtconst.HOUR_MINUTES))
    if milliseconds:
        misec_str = str((minutes + 0.01) - int(minutes)).split(".")[1][:2]
        if len(misec_str) == 1: misec_str += "0"
        misec_str = str(int(int(int(misec_str)) / 10 * 6))
        misec_str = zero_prefix(misec_str)
    result_hrstr = (
        f"{hour_str}:{min_str}{suffix}" if not milliseconds else
        f"{hour_str}:{min_str}:{misec_str}{suffix}"
    )
    return result_hrstr


def print_df_columns_for_constants(df: DataFrame) -> None:
    """
    Prints all df columns with a preparated constant name.
    This is just a helper function to get formated constant names
    with the column names as variable value.
    """
    def prep_const_name(column_name: str) -> str:
        re_values = ". - * + # , ; < > ? ! § $ % & / ( ) = ? ` ´ : ' @ \"".split()  # noqa
        for re_value in re_values:
            column_name = column_name.replace(re_value, "_")

        column_name = column_name.replace(" ", "_")
        while column_name.find("__") != -1:
            column_name = column_name.replace("__", "_")

        for i in range(len(column_name) - 1, 0, -1):
            is_upper_lower = (
                column_name[i].isupper() and
                column_name[i - 1].islower()
            )
            if is_upper_lower:
                column_name = f"{column_name[:i]}_{column_name[i:]}"

        column_name = column_name.upper()
        if column_name[-1] == "_":
            column_name = column_name[:-1]

        return f"DFC_{column_name}"

    print_str = ""
    for column in df.columns:
        const_name = prep_const_name(column)
        print_str += f'{const_name} = "{column}"\n'

    print(print_str)
