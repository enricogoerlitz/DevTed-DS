"""
General utils
"""
import devted.const as dtconst

from typing import Union


def zero_prefix(number_text: str) -> str:
    return f"0{number_text}" if int(number_text) < 10 else f"{number_text}"


def hrstr(
    minutes: Union[float, int],
    suffix: str = "h",
    milliseconds: bool = False
) -> str:
    misec = zero_prefix(int(minutes) - minutes)
    hour_string = zero_prefix(int(minutes / dtconst.HOUR_MINUTES))
    minutes_string = zero_prefix(int(minutes % dtconst.HOUR_MINUTES))
    result_hrstr = (
        f"{hour_string}:{minutes_string}{suffix}" if not milliseconds else
        f"{hour_string}:{minutes_string}:{misec}{suffix}"
    )
    return result_hrstr


# 15:05h
# 15:05:30h
