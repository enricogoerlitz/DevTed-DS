"""
General utils
"""


def zero_prefix(number_text: str) -> str:
    return f"0{number_text}" if int(number_text) < 10 else f"{number_text}"

# def hrstr(minutes, suffix="h", usfmt=False, milliseconds=False)
# def get_hours_string(minutes: float | int) -> str:
#     hour_string  = zero_prefix(int(minutes / HOUR_MINUTES))
#     minutes_string = zero_prefix(int(minutes % HOUR_MINUTES))
#     return f"{hour_string}:{minutes_string}h"
