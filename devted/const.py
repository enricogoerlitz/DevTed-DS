UNNAMED = "Unnamed: 0"

COUNT = "count"
MEAN = "mean"
SUM = "sum"
MEDIAN = "median"
MIN = "min"
MAX = "max"

TOP = "Top"
HIGH = "High"
MEDIUM = "Medium"
LOW = "Low"

CATEGORY = "category"

DAY = "day"
DAYS = "days"
WEEK = "week"
WEEKS = "weeks"
MONTH = "month"
MONTHS = "months"
YEAR = "year"
YEARS = "years"

FIGSIZE_SMALL = (15, 15)
FIGSIZE_MEDIUM = (15, 15)
FIGSIZE_LARGE = (15, 15)
FIGSIZE_XLARGE = (15, 15)

MAP_TO_01 = {False: 0, True: 1}
MAP_TO_TF = {0: False, 1: True}

HOUR_OF_DAY = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14,
    15, 16, 17, 18,
    19, 20, 21, 22, 23
]
DAYS_OF_WEEK_SHORT = [
    "Mon", "Tue", "Wed",
    "Thu", "Fri", "Sat", "Sun"
]
DAYS_OF_WEEK_Full = [
    "Monday", "Tuesday",
    "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
]
MONTHS_OF_YEAR_SHORT = [
    "Jan", "Feb", "Mar",
    "Apr", "May", "Jun",
    "Jul", "Aug", "Sep",
    "Oct", "Nov", "Dec"
]
MONTHS_OF_YEAR_FULL = [
    "January", "February",
    "March", "April",
    "May", "June",
    "July", "August",
    "September", "October",
    "November", "December"
]


SECOND_MILLISECONDS = 1000

MINUTE_SECONDS = 60
MINUTE_MILLISECONDS = SECOND_MILLISECONDS * MINUTE_SECONDS

HOUR_MINUTES = 60
HOUR_SECONDS = HOUR_MINUTES * MINUTE_SECONDS
HOUR_MILLISECONDS = HOUR_SECONDS * SECOND_MILLISECONDS

DAY_HOURS = 24
DAY_MINUTES = DAY_HOURS * HOUR_MINUTES
DAY_SECONDS = DAY_MINUTES * MINUTE_SECONDS
DAY_MILLISECONDS = DAY_SECONDS * SECOND_MILLISECONDS
