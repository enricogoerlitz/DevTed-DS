"""
Data for unittests
"""
import pandas as pd
import numpy


DATA_TITANIC = pd.DataFrame({
    "Survived": [0,
    1,
    1,
    1,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    1,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    1,
    0,
    1,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    1,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    0,
    0,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    1,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0],
    "Pclass": [3,
 1,
 3,
 1,
 3,
 1,
 3,
 3,
 2,
 3,
 1,
 3,
 3,
 3,
 2,
 3,
 3,
 2,
 2,
 3,
 1,
 3,
 3,
 1,
 1,
 2,
 1,
 1,
 3,
 3,
 3,
 3,
 2,
 2,
 3,
 3,
 3,
 3,
 1,
 2,
 1,
 2,
 3,
 2,
 3,
 3,
 1,
 1,
 3,
 2,
 3,
 3,
 3,
 2,
 3,
 2,
 3,
 3,
 3,
 2,
 3,
 3,
 3,
 1,
 2,
 3,
 3,
 1,
 3,
 3,
 3,
 1,
 3,
 3,
 1,
 1,
 2,
 2,
 3,
 1,
 3,
 3,
 3,
 3,
 3,
 1,
 3,
 3,
 3,
 3,
 3,
 3,
 2,
 1,
 3,
 2,
 2,
 2,
 1,
 3,
 3,
 3,
 3,
 3,
 3,
 2,
 2,
 2,
 1,
 1,
 3,
 1,
 3,
 3,
 3,
 2,
 2,
 3,
 3,
 2,
 2,
 2,
 1,
 3,
 3,
 1,
 3,
 3,
 3,
 2,
 3,
 3,
 3,
 3,
 3,
 3,
 1,
 3,
 3,
 3,
 1,
 3,
 1,
 2,
 3,
 3,
 2,
 3,
 1,
 3,
 3,
 2,
 2,
 3,
 2,
 1,
 1,
 3,
 2,
 3,
 3,
 3,
 3,
 3,
 3,
 3,
 3,
 1,
 3,
 2,
 3,
 2,
 1,
 3,
 2,
 1,
 2,
 3,
 2,
 3,
 1,
 3,
 2,
 3,
 2,
 1,
 3,
 2,
 3,
 2,
 2,
 2,
 2,
 2,
 2,
 3,
 3,
 1,
 3,
 2,
 1,
 2,
 3,
 1,
 3,
 3,
 3,
 1,
 1,
 2,
 3,
 1,
 1,
 2,
 3,
 3,
 1,
 1,
 3,
 2,
 1,
 1,
 3,
 3,
 3,
 3,
 3,
 3,
 3,
 3,
 3,
 3,
 2,
 3,
 1,
 1,
 2,
 3,
 3,
 3,
 1,
 1,
 3,
 1,
 1,
 2,
 1,
 1,
 1,
 2,
 3,
 2,
 3,
 2,
 2,
 1,
 1,
 3,
 3,
 2,
 2,
 1,
 3,
 2,
 3,
 1,
 1,
 1,
 3,
 1,
 1,
 3,
 1,
 2,
 1,
 2,
 2,
 2,
 2,
 2,
 3,
 3,
 3,
 3,
 3,
 3,
 1,
 2,
 3,
 2,
 3,
 3,
 3,
 1,
 1,
 1,
 3,
 3,
 1,
 3,
 3,
 1,
 3,
 3,
 1,
 3,
 3,
 1,
 2,
 3,
 2,
 2,
 1,
 3,
 3,
 1,
 3,
 3,
 3,
 2,
 2,
 2,
 3,
 3,
 3,
 3,
 3,
 2,
 3,
 2,
 3,
 1,
 3,
 2,
 2,
 2,
 3,
 3,
 3,
 3,
 3,
 2,
 2,
 3,
 1,
 2,
 3,
 1,
 1,
 3,
 2,
 1,
 2,
 2,
 3,
 3,
 2,
 1,
 2,
 1,
 3,
 1,
 2,
 1,
 1,
 3,
 1,
 2,
 1,
 3,
 1,
 2,
 3,
 1,
 3,
 3,
 2,
 2,
 3,
 2,
 3,
 3,
 3,
 3,
 3,
 3,
 1,
 1,
 1,
 3,
 3,
 3,
 1,
 1,
 3,
 1,
 1,
 3,
 3,
 3,
 3,
 1,
 1,
 2,
 3,
 3,
 3,
 1,
 1,
 3,
 1,
 2,
 2,
 3,
 1,
 3,
 1,
 3,
 2,
 3,
 2,
 2,
 3,
 3,
 2,
 1,
 1,
 1,
 1,
 3,
 3,
 2,
 1,
 1,
 2,
 3,
 2,
 1,
 2,
 3,
 3,
 1,
 1,
 1,
 3,
 3,
 2,
 3,
 3,
 3,
 3,
 2,
 1,
 1,
 3,
 3,
 2,
 1,
 3,
 2,
 1,
 2,
 1,
 1,
 2,
 1,
 3,
 3,
 1,
 3,
 2,
 3,
 3,
 1,
 2,
 3,
 1,
 3,
 3,
 1,
 2,
 1,
 3,
 3,
 2,
 3,
 3,
 2,
 2,
 3,
 1,
 3,
 3,
 3,
 1,
 2,
 1,
 3,
 1,
 3,
 1,
 3,
 2,
 3,
 2,
 3,
 3,
 1,
 3,
 3,
 1,
 3,
 1,
 3,
 2,
 3,
 3,
 2,
 3,
 2,
 1,
 1,
 3,
 1,
 3,
 3,
 2,
 2,
 3,
 2,
 1,
 2,
 2,
 3,
 3,
 3,
 3,
 1,
 1,
 3,
 3,
 2,
 2,
 3,
 3,
 3,
 1,
 1,
 3,
 3,
 1,
 2,
 3,
 1,
 3,
 1,
 1,
 3,
 3,
 3,
 2,
 2,
 1,
 1,
 1,
 1,
 3,
 2,
 3,
 1,
 2,
 3,
 2,
 3,
 2,
 2,
 1,
 3,
 2,
 2,
 3,
 1,
 3,
 2,
 2,
 3,
 3,
 1,
 1,
 1,
 3,
 3,
 1,
 3,
 2,
 1,
 3,
 2,
 3,
 3,
 3,
 2,
 2,
 3,
 2,
 3,
 1,
 3,
 3,
 1,
 3,
 1,
 3,
 3,
 3,
 3,
 2,
 2,
 3,
 3,
 1,
 3,
 1,
 1,
 3,
 3,
 3,
 3,
 3,
 1,
 2,
 3,
 2,
 1,
 3,
 3,
 3,
 2,
 2,
 1,
 3,
 3,
 3,
 1,
 3,
 2,
 1,
 3,
 3,
 2,
 3,
 3,
 3,
 2,
 3,
 3,
 1,
 3,
 1,
 3,
 3,
 2,
 1,
 3,
 2,
 3,
 3,
 1,
 3,
 3,
 3,
 2,
 1,
 3,
 3,
 3,
 3,
 2,
 3,
 3,
 3,
 1,
 2,
 3,
 1,
 1,
 3,
 3,
 2,
 1,
 2,
 2,
 2,
 1,
 3,
 3,
 1,
 1,
 3,
 2,
 3,
 3,
 3,
 1,
 2,
 3,
 3,
 2,
 3,
 3,
 2,
 1,
 1,
 3],
    "Age": [22.0,
 38.0,
 26.0,
 35.0,
 35.0,
 54.0,
 2.0,
 27.0,
 14.0,
 4.0,
 58.0,
 20.0,
 39.0,
 14.0,
 55.0,
 2.0,
 31.0,
 35.0,
 34.0,
 15.0,
 28.0,
 8.0,
 38.0,
 19.0,
 40.0,
 66.0,
 28.0,
 42.0,
 21.0,
 18.0,
 14.0,
 40.0,
 27.0,
 3.0,
 19.0,
 18.0,
 7.0,
 21.0,
 49.0,
 29.0,
 65.0,
 21.0,
 28.5,
 5.0,
 11.0,
 22.0,
 38.0,
 45.0,
 4.0,
 29.0,
 19.0,
 17.0,
 26.0,
 32.0,
 16.0,
 21.0,
 26.0,
 32.0,
 25.0,
 0.83,
 30.0,
 22.0,
 29.0,
 28.0,
 17.0,
 33.0,
 16.0,
 23.0,
 24.0,
 29.0,
 20.0,
 46.0,
 26.0,
 59.0,
 71.0,
 23.0,
 34.0,
 34.0,
 28.0,
 21.0,
 33.0,
 37.0,
 28.0,
 21.0,
 38.0,
 47.0,
 14.5,
 22.0,
 20.0,
 17.0,
 21.0,
 70.5,
 29.0,
 24.0,
 2.0,
 21.0,
 32.5,
 32.5,
 54.0,
 12.0,
 24.0,
 45.0,
 33.0,
 20.0,
 47.0,
 29.0,
 25.0,
 23.0,
 19.0,
 37.0,
 16.0,
 24.0,
 22.0,
 24.0,
 19.0,
 18.0,
 19.0,
 27.0,
 9.0,
 36.5,
 42.0,
 51.0,
 22.0,
 55.5,
 40.5,
 51.0,
 16.0,
 30.0,
 44.0,
 40.0,
 26.0,
 17.0,
 1.0,
 9.0,
 45.0,
 28.0,
 61.0,
 4.0,
 1.0,
 21.0,
 56.0,
 18.0,
 50.0,
 30.0,
 36.0,
 9.0,
 1.0,
 4.0,
 45.0,
 40.0,
 36.0,
 32.0,
 19.0,
 19.0,
 3.0,
 44.0,
 58.0,
 42.0,
 24.0,
 28.0,
 34.0,
 45.5,
 18.0,
 2.0,
 32.0,
 26.0,
 16.0,
 40.0,
 24.0,
 35.0,
 22.0,
 30.0,
 31.0,
 27.0,
 42.0,
 32.0,
 30.0,
 16.0,
 27.0,
 51.0,
 38.0,
 22.0,
 19.0,
 20.5,
 18.0,
 35.0,
 29.0,
 59.0,
 5.0,
 24.0,
 44.0,
 8.0,
 19.0,
 33.0,
 29.0,
 22.0,
 30.0,
 44.0,
 25.0,
 24.0,
 37.0,
 54.0,
 29.0,
 62.0,
 30.0,
 41.0,
 29.0,
 30.0,
 35.0,
 50.0,
 3.0,
 52.0,
 40.0,
 36.0,
 16.0,
 25.0,
 58.0,
 35.0,
 25.0,
 41.0,
 37.0,
 63.0,
 45.0,
 7.0,
 35.0,
 65.0,
 28.0,
 16.0,
 19.0,
 33.0,
 30.0,
 22.0,
 42.0,
 22.0,
 26.0,
 19.0,
 36.0,
 24.0,
 24.0,
 23.5,
 2.0,
 50.0,
 19.0,
 0.92,
 17.0,
 30.0,
 30.0,
 24.0,
 18.0,
 26.0,
 28.0,
 43.0,
 26.0,
 24.0,
 54.0,
 31.0,
 40.0,
 22.0,
 27.0,
 30.0,
 22.0,
 36.0,
 61.0,
 36.0,
 31.0,
 16.0,
 45.5,
 38.0,
 16.0,
 29.0,
 41.0,
 45.0,
 45.0,
 2.0,
 24.0,
 28.0,
 25.0,
 36.0,
 24.0,
 40.0,
 3.0,
 42.0,
 23.0,
 15.0,
 25.0,
 28.0,
 22.0,
 38.0,
 40.0,
 29.0,
 45.0,
 35.0,
 30.0,
 60.0,
 24.0,
 25.0,
 18.0,
 19.0,
 22.0,
 3.0,
 22.0,
 27.0,
 20.0,
 19.0,
 42.0,
 1.0,
 32.0,
 35.0,
 18.0,
 1.0,
 36.0,
 17.0,
 36.0,
 21.0,
 28.0,
 23.0,
 24.0,
 22.0,
 31.0,
 46.0,
 23.0,
 28.0,
 39.0,
 26.0,
 21.0,
 28.0,
 20.0,
 34.0,
 51.0,
 3.0,
 21.0,
 33.0,
 44.0,
 34.0,
 18.0,
 30.0,
 10.0,
 21.0,
 29.0,
 28.0,
 18.0,
 28.0,
 19.0,
 32.0,
 28.0,
 42.0,
 17.0,
 50.0,
 14.0,
 21.0,
 24.0,
 64.0,
 31.0,
 45.0,
 20.0,
 25.0,
 28.0,
 4.0,
 13.0,
 34.0,
 5.0,
 52.0,
 36.0,
 30.0,
 49.0,
 29.0,
 65.0,
 50.0,
 48.0,
 34.0,
 47.0,
 48.0,
 38.0,
 56.0,
 0.75,
 38.0,
 33.0,
 23.0,
 22.0,
 34.0,
 29.0,
 22.0,
 2.0,
 9.0,
 50.0,
 63.0,
 25.0,
 35.0,
 58.0,
 30.0,
 9.0,
 21.0,
 55.0,
 71.0,
 21.0,
 54.0,
 25.0,
 24.0,
 17.0,
 21.0,
 37.0,
 16.0,
 18.0,
 33.0,
 28.0,
 26.0,
 29.0,
 36.0,
 54.0,
 24.0,
 47.0,
 34.0,
 36.0,
 32.0,
 30.0,
 22.0,
 44.0,
 40.5,
 50.0,
 39.0,
 23.0,
 2.0,
 17.0,
 30.0,
 7.0,
 45.0,
 30.0,
 22.0,
 36.0,
 9.0,
 11.0,
 32.0,
 50.0,
 64.0,
 19.0,
 33.0,
 8.0,
 17.0,
 27.0,
 22.0,
 22.0,
 62.0,
 48.0,
 39.0,
 36.0,
 40.0,
 28.0,
 24.0,
 19.0,
 29.0,
 32.0,
 62.0,
 53.0,
 36.0,
 16.0,
 19.0,
 34.0,
 39.0,
 32.0,
 25.0,
 39.0,
 54.0,
 36.0,
 18.0,
 47.0,
 60.0,
 22.0,
 35.0,
 52.0,
 47.0,
 37.0,
 36.0,
 49.0,
 49.0,
 24.0,
 44.0,
 35.0,
 36.0,
 30.0,
 27.0,
 22.0,
 40.0,
 39.0,
 35.0,
 24.0,
 34.0,
 26.0,
 4.0,
 26.0,
 27.0,
 42.0,
 20.0,
 21.0,
 21.0,
 61.0,
 57.0,
 21.0,
 26.0,
 80.0,
 51.0,
 32.0,
 9.0,
 28.0,
 32.0,
 31.0,
 41.0,
 20.0,
 24.0,
 2.0,
 0.75,
 48.0,
 19.0,
 56.0,
 23.0,
 18.0,
 21.0,
 18.0,
 24.0,
 32.0,
 23.0,
 58.0,
 50.0,
 40.0,
 47.0,
 36.0,
 20.0,
 32.0,
 25.0,
 43.0,
 40.0,
 31.0,
 70.0,
 31.0,
 18.0,
 24.5,
 18.0,
 43.0,
 36.0,
 27.0,
 20.0,
 14.0,
 60.0,
 25.0,
 14.0,
 19.0,
 18.0,
 15.0,
 31.0,
 4.0,
 25.0,
 60.0,
 52.0,
 44.0,
 49.0,
 42.0,
 18.0,
 35.0,
 18.0,
 25.0,
 26.0,
 39.0,
 45.0,
 42.0,
 22.0,
 24.0,
 48.0,
 29.0,
 52.0,
 19.0,
 38.0,
 27.0,
 33.0,
 6.0,
 17.0,
 34.0,
 50.0,
 27.0,
 20.0,
 30.0,
 25.0,
 25.0,
 29.0,
 11.0,
 23.0,
 23.0,
 28.5,
 48.0,
 35.0,
 36.0,
 21.0,
 24.0,
 31.0,
 70.0,
 16.0,
 30.0,
 19.0,
 31.0,
 4.0,
 6.0,
 33.0,
 23.0,
 48.0,
 0.67,
 28.0,
 18.0,
 34.0,
 33.0,
 41.0,
 20.0,
 36.0,
 16.0,
 51.0,
 30.5,
 32.0,
 24.0,
 48.0,
 57.0,
 54.0,
 18.0,
 5.0,
 43.0,
 13.0,
 17.0,
 29.0,
 25.0,
 25.0,
 18.0,
 8.0,
 1.0,
 46.0,
 16.0,
 25.0,
 39.0,
 49.0,
 31.0,
 30.0,
 30.0,
 34.0,
 31.0,
 11.0,
 0.42,
 27.0,
 31.0,
 39.0,
 18.0,
 39.0,
 33.0,
 26.0,
 39.0,
 35.0,
 6.0,
 30.5,
 23.0,
 31.0,
 43.0,
 10.0,
 52.0,
 27.0,
 38.0,
 27.0,
 2.0,
 1.0,
 62.0,
 15.0,
 0.83,
 23.0,
 18.0,
 39.0,
 21.0,
 32.0,
 20.0,
 16.0,
 30.0,
 34.5,
 17.0,
 42.0,
 35.0,
 28.0,
 4.0,
 74.0,
 9.0,
 16.0,
 44.0,
 18.0,
 45.0,
 51.0,
 24.0,
 41.0,
 21.0,
 48.0,
 24.0,
 42.0,
 27.0,
 31.0,
 4.0,
 26.0,
 47.0,
 33.0,
 47.0,
 28.0,
 15.0,
 20.0,
 19.0,
 56.0,
 25.0,
 33.0,
 22.0,
 28.0,
 25.0,
 39.0,
 27.0,
 19.0,
 26.0,
 32.0],
    "Embarked": ['S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'C',
 'Q',
 'S',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'C',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'C',
 'S',
 'Q',
 'S',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'C',
 'Q',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'Q',
 'S',
 'Q',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'C',
 'C',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'C',
 'C',
 'C',
 'C',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'Q',
 'S',
 'C',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'C',
 'S',
 'S',
 'C',
 'C',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'C',
 'C',
 'S',
 'C',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'C',
 'C',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'C',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'C',
 'C',
 'S',
 'C',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'Q',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'C',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'C',
 'S',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'C',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'C',
 'C',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'C',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'S',
 'C',
 'C',
 'S',
 'S',
 'C',
 'S',
 'S',
 'S',
 'S',
 'S',
 'Q',
 'S',
 'S',
 'C',
 'Q'],
 "Fare": [7.25,
 71.2833,
 7.925,
 53.1,
 8.05,
 51.8625,
 21.075,
 11.1333,
 30.0708,
 16.7,
 26.55,
 8.05,
 31.275,
 7.8542,
 16.0,
 29.125,
 18.0,
 26.0,
 13.0,
 8.0292,
 35.5,
 21.075,
 31.3875,
 263.0,
 27.7208,
 10.5,
 82.1708,
 52.0,
 8.05,
 18.0,
 11.2417,
 9.475,
 21.0,
 41.5792,
 7.8792,
 17.8,
 39.6875,
 7.8,
 76.7292,
 26.0,
 61.9792,
 10.5,
 7.2292,
 27.75,
 46.9,
 7.2292,
 80.0,
 83.475,
 27.9,
 10.5,
 8.1583,
 7.925,
 8.6625,
 10.5,
 46.9,
 73.5,
 14.4542,
 56.4958,
 7.65,
 29.0,
 12.475,
 9.0,
 9.5,
 47.1,
 10.5,
 15.85,
 34.375,
 263.0,
 8.05,
 8.05,
 7.8542,
 61.175,
 20.575,
 7.25,
 34.6542,
 63.3583,
 23.0,
 26.0,
 7.8958,
 77.2875,
 8.6542,
 7.925,
 7.8958,
 7.65,
 7.8958,
 52.0,
 14.4542,
 8.05,
 9.825,
 14.4583,
 7.925,
 7.75,
 21.0,
 247.5208,
 31.275,
 73.5,
 30.0708,
 13.0,
 77.2875,
 11.2417,
 7.1417,
 6.975,
 7.8958,
 7.05,
 14.5,
 26.0,
 13.0,
 15.0458,
 26.2833,
 53.1,
 9.2167,
 79.2,
 7.75,
 15.85,
 6.75,
 11.5,
 36.75,
 7.7958,
 34.375,
 26.0,
 13.0,
 12.525,
 66.6,
 8.05,
 14.5,
 61.3792,
 7.7333,
 8.05,
 16.1,
 15.75,
 7.775,
 8.6625,
 39.6875,
 20.525,
 27.9,
 56.4958,
 33.5,
 29.125,
 11.1333,
 7.925,
 30.6958,
 7.8542,
 28.7125,
 13.0,
 0.0,
 31.3875,
 39.0,
 22.025,
 26.55,
 15.5,
 7.8958,
 13.0,
 13.0,
 7.8542,
 26.0,
 27.7208,
 146.5208,
 8.4042,
 13.0,
 9.5,
 6.4958,
 7.225,
 8.05,
 10.4625,
 15.85,
 18.7875,
 7.75,
 31.0,
 7.05,
 21.0,
 7.25,
 13.0,
 113.275,
 7.925,
 27.0,
 76.2917,
 10.5,
 8.05,
 13.0,
 8.05,
 90.0,
 9.35,
 10.5,
 7.25,
 13.0,
 83.475,
 7.775,
 13.5,
 31.3875,
 10.5,
 26.0,
 26.25,
 10.5,
 12.275,
 10.5,
 7.125,
 7.225,
 90.0,
 7.775,
 14.5,
 52.5542,
 26.0,
 10.4625,
 26.55,
 16.1,
 20.2125,
 15.2458,
 86.5,
 512.3292,
 26.0,
 31.3875,
 79.65,
 0.0,
 10.5,
 39.6875,
 7.775,
 153.4625,
 135.6333,
 0.0,
 19.5,
 29.7,
 77.9583,
 7.75,
 29.125,
 20.25,
 7.75,
 7.8542,
 9.5,
 8.05,
 8.6625,
 9.5,
 7.8958,
 13.0,
 7.75,
 78.85,
 91.0792,
 12.875,
 8.85,
 7.8958,
 7.2292,
 151.55,
 247.5208,
 0.0,
 151.55,
 108.9,
 24.0,
 56.9292,
 83.1583,
 262.375,
 26.0,
 7.8958,
 26.25,
 7.8542,
 26.0,
 14.0,
 164.8667,
 134.5,
 7.25,
 7.8958,
 12.35,
 29.0,
 135.6333,
 6.2375,
 13.0,
 20.525,
 57.9792,
 28.5,
 153.4625,
 18.0,
 66.6,
 134.5,
 8.05,
 35.5,
 26.0,
 263.0,
 13.0,
 13.0,
 13.0,
 13.0,
 13.0,
 15.9,
 8.6625,
 9.225,
 7.2292,
 17.8,
 9.5,
 55.0,
 13.0,
 27.9,
 27.7208,
 14.4542,
 7.05,
 7.25,
 75.25,
 69.3,
 55.4417,
 6.4958,
 8.05,
 135.6333,
 21.075,
 7.25,
 211.5,
 4.0125,
 7.775,
 227.525,
 15.7417,
 7.925,
 52.0,
 73.5,
 46.9,
 13.0,
 12.0,
 120.0,
 7.7958,
 7.925,
 113.275,
 16.7,
 7.7958,
 7.8542,
 26.0,
 10.5,
 12.65,
 7.925,
 8.05,
 9.825,
 15.85,
 8.6625,
 21.0,
 7.75,
 18.75,
 7.775,
 90.0,
 7.925,
 32.5,
 13.0,
 13.0,
 24.15,
 7.7333,
 7.875,
 14.4,
 20.2125,
 26.0,
 26.0,
 8.05,
 26.55,
 26.0,
 7.125,
 55.9,
 120.0,
 34.375,
 18.75,
 263.0,
 10.5,
 26.25,
 9.5,
 7.775,
 13.0,
 81.8583,
 19.5,
 26.55,
 19.2583,
 30.5,
 27.75,
 27.75,
 89.1042,
 7.8958,
 26.55,
 10.5,
 26.55,
 8.05,
 38.5,
 13.0,
 7.05,
 26.55,
 19.2583,
 8.6625,
 27.75,
 13.7917,
 9.8375,
 21.0,
 7.0458,
 7.5208,
 12.2875,
 46.9,
 8.05,
 9.5875,
 91.0792,
 90.0,
 29.7,
 8.05,
 15.9,
 7.25,
 30.5,
 49.5042,
 8.05,
 78.2667,
 151.55,
 7.7958,
 8.6625,
 7.75,
 9.5875,
 86.5,
 108.9,
 26.0,
 22.525,
 56.4958,
 7.75,
 26.2875,
 59.4,
 7.4958,
 34.0208,
 10.5,
 26.0,
 7.8958,
 93.5,
 7.8958,
 57.9792,
 7.75,
 10.5,
 7.925,
 11.5,
 26.0,
 7.2292,
 8.6625,
 26.25,
 26.55,
 106.425,
 49.5,
 71.0,
 31.275,
 31.275,
 26.0,
 106.425,
 26.0,
 26.0,
 20.525,
 36.75,
 110.8833,
 26.0,
 7.225,
 7.775,
 26.55,
 39.6,
 79.65,
 17.4,
 7.8958,
 13.5,
 24.15,
 7.8958,
 21.075,
 7.8542,
 10.5,
 51.4792,
 26.3875,
 8.05,
 14.5,
 13.0,
 55.9,
 7.925,
 30.0,
 110.8833,
 26.0,
 40.125,
 79.65,
 15.0,
 79.2,
 8.05,
 7.125,
 78.2667,
 7.25,
 26.0,
 24.15,
 0.0,
 56.9292,
 27.0,
 8.05,
 26.55,
 15.55,
 7.8958,
 30.5,
 41.5792,
 153.4625,
 31.275,
 8.05,
 65.0,
 14.4,
 16.1,
 39.0,
 10.5,
 14.4542,
 52.5542,
 15.7417,
 7.8542,
 16.1,
 32.3208,
 12.35,
 77.9583,
 7.8958,
 30.0,
 7.0542,
 30.5,
 27.9,
 13.0,
 7.925,
 26.25,
 39.6875,
 7.8542,
 69.3,
 27.9,
 19.2583,
 76.7292,
 7.8958,
 35.5,
 7.55,
 23.0,
 8.4333,
 6.75,
 73.5,
 15.5,
 13.0,
 113.275,
 133.65,
 7.225,
 25.5875,
 7.4958,
 7.925,
 73.5,
 13.0,
 8.05,
 39.0,
 52.0,
 10.5,
 13.0,
 7.775,
 8.05,
 9.8417,
 46.9,
 512.3292,
 76.7292,
 9.225,
 46.9,
 39.0,
 41.5792,
 39.6875,
 10.1708,
 7.7958,
 211.3375,
 57.0,
 13.4167,
 7.225,
 26.55,
 13.5,
 8.05,
 110.8833,
 7.65,
 227.525,
 26.2875,
 14.4542,
 7.7417,
 7.8542,
 26.0,
 13.5,
 26.2875,
 151.55,
 49.5042,
 52.0,
 9.4833,
 13.0,
 7.65,
 227.525,
 10.5,
 7.775,
 33.0,
 7.0542,
 13.0,
 13.0,
 53.1,
 8.6625,
 21.0,
 26.0,
 7.925,
 211.3375,
 18.7875,
 13.0,
 13.0,
 16.1,
 34.375,
 512.3292,
 78.85,
 262.375,
 16.1,
 7.925,
 71.0,
 20.25,
 13.0,
 53.1,
 7.75,
 23.0,
 12.475,
 9.5,
 7.8958,
 65.0,
 14.5,
 7.7958,
 11.5,
 8.05,
 86.5,
 7.125,
 7.2292,
 120.0,
 7.775,
 77.9583,
 7.75,
 8.3625,
 9.5,
 7.8542,
 10.5,
 23.0,
 7.75,
 12.475,
 211.3375,
 7.2292,
 57.0,
 30.0,
 7.05,
 7.25,
 7.4958,
 29.125,
 20.575,
 79.2,
 26.0,
 7.8958,
 13.0,
 25.9292,
 8.6833,
 7.2292,
 24.15,
 13.0,
 26.25,
 120.0,
 8.5167,
 6.975,
 7.775,
 0.0,
 7.775,
 13.0,
 53.1,
 7.8875,
 24.15,
 10.5,
 31.275,
 8.05,
 7.925,
 37.0042,
 6.45,
 27.9,
 93.5,
 8.6625,
 0.0,
 12.475,
 39.6875,
 37.0042,
 80.0,
 14.4542,
 18.75,
 7.8542,
 8.3,
 83.1583,
 8.6625,
 56.4958,
 7.925,
 10.5,
 31.0,
 6.4375,
 8.6625,
 7.55,
 7.8958,
 33.0,
 31.275,
 7.775,
 15.2458,
 39.4,
 26.0,
 9.35,
 164.8667,
 26.55,
 19.2583,
 14.1083,
 11.5,
 25.9292,
 13.0,
 13.0,
 13.8583,
 50.4958,
 11.1333,
 7.8958,
 52.5542,
 5.0,
 9.0,
 24.0,
 7.225,
 9.8458,
 7.8958,
 83.1583,
 26.0,
 7.8958,
 10.5167,
 10.5,
 7.05,
 29.125,
 13.0,
 30.0,
 30.0,
 7.75],
})

DATA_TIMESERIES = pd.DataFrame({
   "Date": [numpy.datetime64('2021-11-15T00:00:00.000000000'),
 numpy.datetime64('2021-11-16T00:00:00.000000000'),
 numpy.datetime64('2021-11-17T00:00:00.000000000'),
 numpy.datetime64('2021-11-18T00:00:00.000000000'),
 numpy.datetime64('2021-11-19T00:00:00.000000000'),
 numpy.datetime64('2021-11-22T00:00:00.000000000'),
 numpy.datetime64('2021-11-23T00:00:00.000000000'),
 numpy.datetime64('2021-11-24T00:00:00.000000000'),
 numpy.datetime64('2021-11-26T00:00:00.000000000'),
 numpy.datetime64('2021-11-29T00:00:00.000000000'),
 numpy.datetime64('2021-11-30T00:00:00.000000000'),
 numpy.datetime64('2021-12-01T00:00:00.000000000'),
 numpy.datetime64('2021-12-02T00:00:00.000000000'),
 numpy.datetime64('2021-12-03T00:00:00.000000000'),
 numpy.datetime64('2021-12-06T00:00:00.000000000'),
 numpy.datetime64('2021-12-07T00:00:00.000000000'),
 numpy.datetime64('2021-12-08T00:00:00.000000000'),
 numpy.datetime64('2021-12-09T00:00:00.000000000'),
 numpy.datetime64('2021-12-10T00:00:00.000000000'),
 numpy.datetime64('2021-12-13T00:00:00.000000000'),
 numpy.datetime64('2021-12-14T00:00:00.000000000'),
 numpy.datetime64('2021-12-15T00:00:00.000000000'),
 numpy.datetime64('2021-12-16T00:00:00.000000000'),
 numpy.datetime64('2021-12-17T00:00:00.000000000'),
 numpy.datetime64('2021-12-20T00:00:00.000000000'),
 numpy.datetime64('2021-12-21T00:00:00.000000000'),
 numpy.datetime64('2021-12-22T00:00:00.000000000'),
 numpy.datetime64('2021-12-23T00:00:00.000000000'),
 numpy.datetime64('2021-12-27T00:00:00.000000000'),
 numpy.datetime64('2021-12-28T00:00:00.000000000'),
 numpy.datetime64('2021-12-29T00:00:00.000000000'),
 numpy.datetime64('2021-12-30T00:00:00.000000000'),
 numpy.datetime64('2021-12-31T00:00:00.000000000'),
 numpy.datetime64('2022-01-03T00:00:00.000000000'),
 numpy.datetime64('2022-01-04T00:00:00.000000000'),
 numpy.datetime64('2022-01-05T00:00:00.000000000'),
 numpy.datetime64('2022-01-06T00:00:00.000000000'),
 numpy.datetime64('2022-01-07T00:00:00.000000000'),
 numpy.datetime64('2022-01-10T00:00:00.000000000'),
 numpy.datetime64('2022-01-11T00:00:00.000000000'),
 numpy.datetime64('2022-01-12T00:00:00.000000000'),
 numpy.datetime64('2022-01-13T00:00:00.000000000'),
 numpy.datetime64('2022-01-14T00:00:00.000000000'),
 numpy.datetime64('2022-01-18T00:00:00.000000000'),
 numpy.datetime64('2022-01-19T00:00:00.000000000'),
 numpy.datetime64('2022-01-20T00:00:00.000000000'),
 numpy.datetime64('2022-01-21T00:00:00.000000000'),
 numpy.datetime64('2022-01-24T00:00:00.000000000'),
 numpy.datetime64('2022-01-25T00:00:00.000000000'),
 numpy.datetime64('2022-01-26T00:00:00.000000000'),
 numpy.datetime64('2022-01-27T00:00:00.000000000'),
 numpy.datetime64('2022-01-28T00:00:00.000000000'),
 numpy.datetime64('2022-01-31T00:00:00.000000000'),
 numpy.datetime64('2022-02-01T00:00:00.000000000'),
 numpy.datetime64('2022-02-02T00:00:00.000000000'),
 numpy.datetime64('2022-02-03T00:00:00.000000000'),
 numpy.datetime64('2022-02-04T00:00:00.000000000'),
 numpy.datetime64('2022-02-07T00:00:00.000000000'),
 numpy.datetime64('2022-02-08T00:00:00.000000000'),
 numpy.datetime64('2022-02-09T00:00:00.000000000'),
 numpy.datetime64('2022-02-10T00:00:00.000000000'),
 numpy.datetime64('2022-02-11T00:00:00.000000000'),
 numpy.datetime64('2022-02-14T00:00:00.000000000'),
 numpy.datetime64('2022-02-15T00:00:00.000000000'),
 numpy.datetime64('2022-02-16T00:00:00.000000000'),
 numpy.datetime64('2022-02-17T00:00:00.000000000'),
 numpy.datetime64('2022-02-18T00:00:00.000000000'),
 numpy.datetime64('2022-02-22T00:00:00.000000000'),
 numpy.datetime64('2022-02-23T00:00:00.000000000'),
 numpy.datetime64('2022-02-24T00:00:00.000000000'),
 numpy.datetime64('2022-02-25T00:00:00.000000000'),
 numpy.datetime64('2022-02-28T00:00:00.000000000'),
 numpy.datetime64('2022-03-01T00:00:00.000000000'),
 numpy.datetime64('2022-03-02T00:00:00.000000000'),
 numpy.datetime64('2022-03-03T00:00:00.000000000'),
 numpy.datetime64('2022-03-04T00:00:00.000000000'),
 numpy.datetime64('2022-03-07T00:00:00.000000000'),
 numpy.datetime64('2022-03-08T00:00:00.000000000'),
 numpy.datetime64('2022-03-09T00:00:00.000000000'),
 numpy.datetime64('2022-03-10T00:00:00.000000000'),
 numpy.datetime64('2022-03-11T00:00:00.000000000'),
 numpy.datetime64('2022-03-14T00:00:00.000000000'),
 numpy.datetime64('2022-03-15T00:00:00.000000000'),
 numpy.datetime64('2022-03-16T00:00:00.000000000'),
 numpy.datetime64('2022-03-17T00:00:00.000000000'),
 numpy.datetime64('2022-03-18T00:00:00.000000000'),
 numpy.datetime64('2022-03-21T00:00:00.000000000'),
 numpy.datetime64('2022-03-22T00:00:00.000000000'),
 numpy.datetime64('2022-03-23T00:00:00.000000000'),
 numpy.datetime64('2022-03-24T00:00:00.000000000'),
 numpy.datetime64('2022-03-25T00:00:00.000000000'),
 numpy.datetime64('2022-03-28T00:00:00.000000000'),
 numpy.datetime64('2022-03-29T00:00:00.000000000'),
 numpy.datetime64('2022-03-30T00:00:00.000000000'),
 numpy.datetime64('2022-03-31T00:00:00.000000000'),
 numpy.datetime64('2022-04-01T00:00:00.000000000'),
 numpy.datetime64('2022-04-04T00:00:00.000000000'),
 numpy.datetime64('2022-04-05T00:00:00.000000000'),
 numpy.datetime64('2022-04-06T00:00:00.000000000'),
 numpy.datetime64('2022-04-07T00:00:00.000000000'),
 numpy.datetime64('2022-04-08T00:00:00.000000000'),
 numpy.datetime64('2022-04-11T00:00:00.000000000'),
 numpy.datetime64('2022-04-12T00:00:00.000000000'),
 numpy.datetime64('2022-04-13T00:00:00.000000000'),
 numpy.datetime64('2022-04-14T00:00:00.000000000'),
 numpy.datetime64('2022-04-18T00:00:00.000000000'),
 numpy.datetime64('2022-04-19T00:00:00.000000000'),
 numpy.datetime64('2022-04-20T00:00:00.000000000'),
 numpy.datetime64('2022-04-21T00:00:00.000000000'),
 numpy.datetime64('2022-04-22T00:00:00.000000000'),
 numpy.datetime64('2022-04-25T00:00:00.000000000'),
 numpy.datetime64('2022-04-26T00:00:00.000000000'),
 numpy.datetime64('2022-04-27T00:00:00.000000000'),
 numpy.datetime64('2022-04-28T00:00:00.000000000'),
 numpy.datetime64('2022-04-29T00:00:00.000000000'),
 numpy.datetime64('2022-05-02T00:00:00.000000000'),
 numpy.datetime64('2022-05-03T00:00:00.000000000'),
 numpy.datetime64('2022-05-04T00:00:00.000000000'),
 numpy.datetime64('2022-05-05T00:00:00.000000000'),
 numpy.datetime64('2022-05-06T00:00:00.000000000'),
 numpy.datetime64('2022-05-09T00:00:00.000000000'),
 numpy.datetime64('2022-05-10T00:00:00.000000000'),
 numpy.datetime64('2022-05-11T00:00:00.000000000'),
 numpy.datetime64('2022-05-12T00:00:00.000000000'),
 numpy.datetime64('2022-05-13T00:00:00.000000000'),
 numpy.datetime64('2022-05-16T00:00:00.000000000'),
 numpy.datetime64('2022-05-17T00:00:00.000000000'),
 numpy.datetime64('2022-05-18T00:00:00.000000000'),
 numpy.datetime64('2022-05-19T00:00:00.000000000'),
 numpy.datetime64('2022-05-20T00:00:00.000000000'),
 numpy.datetime64('2022-05-23T00:00:00.000000000'),
 numpy.datetime64('2022-05-24T00:00:00.000000000'),
 numpy.datetime64('2022-05-25T00:00:00.000000000'),
 numpy.datetime64('2022-05-26T00:00:00.000000000'),
 numpy.datetime64('2022-05-27T00:00:00.000000000'),
 numpy.datetime64('2022-05-31T00:00:00.000000000'),
 numpy.datetime64('2022-06-01T00:00:00.000000000'),
 numpy.datetime64('2022-06-02T00:00:00.000000000'),
 numpy.datetime64('2022-06-03T00:00:00.000000000'),
 numpy.datetime64('2022-06-06T00:00:00.000000000'),
 numpy.datetime64('2022-06-07T00:00:00.000000000'),
 numpy.datetime64('2022-06-08T00:00:00.000000000'),
 numpy.datetime64('2022-06-09T00:00:00.000000000'),
 numpy.datetime64('2022-06-10T00:00:00.000000000'),
 numpy.datetime64('2022-06-13T00:00:00.000000000'),
 numpy.datetime64('2022-06-14T00:00:00.000000000'),
 numpy.datetime64('2022-06-15T00:00:00.000000000'),
 numpy.datetime64('2022-06-16T00:00:00.000000000'),
 numpy.datetime64('2022-06-17T00:00:00.000000000'),
 numpy.datetime64('2022-06-21T00:00:00.000000000'),
 numpy.datetime64('2022-06-22T00:00:00.000000000'),
 numpy.datetime64('2022-06-23T00:00:00.000000000'),
 numpy.datetime64('2022-06-24T00:00:00.000000000'),
 numpy.datetime64('2022-06-27T00:00:00.000000000'),
 numpy.datetime64('2022-06-28T00:00:00.000000000'),
 numpy.datetime64('2022-06-29T00:00:00.000000000'),
 numpy.datetime64('2022-06-30T00:00:00.000000000'),
 numpy.datetime64('2022-07-01T00:00:00.000000000'),
 numpy.datetime64('2022-07-05T00:00:00.000000000'),
 numpy.datetime64('2022-07-06T00:00:00.000000000'),
 numpy.datetime64('2022-07-07T00:00:00.000000000'),
 numpy.datetime64('2022-07-08T00:00:00.000000000'),
 numpy.datetime64('2022-07-11T00:00:00.000000000'),
 numpy.datetime64('2022-07-12T00:00:00.000000000'),
 numpy.datetime64('2022-07-13T00:00:00.000000000'),
 numpy.datetime64('2022-07-14T00:00:00.000000000'),
 numpy.datetime64('2022-07-15T00:00:00.000000000'),
 numpy.datetime64('2022-07-18T00:00:00.000000000'),
 numpy.datetime64('2022-07-19T00:00:00.000000000'),
 numpy.datetime64('2022-07-20T00:00:00.000000000'),
 numpy.datetime64('2022-07-21T00:00:00.000000000'),
 numpy.datetime64('2022-07-22T00:00:00.000000000'),
 numpy.datetime64('2022-07-25T00:00:00.000000000'),
 numpy.datetime64('2022-07-26T00:00:00.000000000'),
 numpy.datetime64('2022-07-27T00:00:00.000000000'),
 numpy.datetime64('2022-07-28T00:00:00.000000000'),
 numpy.datetime64('2022-07-29T00:00:00.000000000'),
 numpy.datetime64('2022-08-01T00:00:00.000000000'),
 numpy.datetime64('2022-08-02T00:00:00.000000000'),
 numpy.datetime64('2022-08-03T00:00:00.000000000'),
 numpy.datetime64('2022-08-04T00:00:00.000000000'),
 numpy.datetime64('2022-08-05T00:00:00.000000000'),
 numpy.datetime64('2022-08-08T00:00:00.000000000'),
 numpy.datetime64('2022-08-09T00:00:00.000000000'),
 numpy.datetime64('2022-08-10T00:00:00.000000000'),
 numpy.datetime64('2022-08-11T00:00:00.000000000'),
 numpy.datetime64('2022-08-12T00:00:00.000000000'),
 numpy.datetime64('2022-08-15T00:00:00.000000000'),
 numpy.datetime64('2022-08-16T00:00:00.000000000'),
 numpy.datetime64('2022-08-17T00:00:00.000000000'),
 numpy.datetime64('2022-08-18T00:00:00.000000000'),
 numpy.datetime64('2022-08-19T00:00:00.000000000'),
 numpy.datetime64('2022-08-22T00:00:00.000000000'),
 numpy.datetime64('2022-08-23T00:00:00.000000000'),
 numpy.datetime64('2022-08-24T00:00:00.000000000'),
 numpy.datetime64('2022-08-25T00:00:00.000000000'),
 numpy.datetime64('2022-08-26T00:00:00.000000000'),
 numpy.datetime64('2022-08-29T00:00:00.000000000'),
 numpy.datetime64('2022-08-30T00:00:00.000000000'),
 numpy.datetime64('2022-08-31T00:00:00.000000000'),
 numpy.datetime64('2022-09-01T00:00:00.000000000'),
 numpy.datetime64('2022-09-02T00:00:00.000000000'),
 numpy.datetime64('2022-09-06T00:00:00.000000000'),
 numpy.datetime64('2022-09-07T00:00:00.000000000'),
 numpy.datetime64('2022-09-08T00:00:00.000000000'),
 numpy.datetime64('2022-09-09T00:00:00.000000000'),
 numpy.datetime64('2022-09-12T00:00:00.000000000'),
 numpy.datetime64('2022-09-13T00:00:00.000000000'),
 numpy.datetime64('2022-09-14T00:00:00.000000000'),
 numpy.datetime64('2022-09-15T00:00:00.000000000'),
 numpy.datetime64('2022-09-16T00:00:00.000000000'),
 numpy.datetime64('2022-09-19T00:00:00.000000000'),
 numpy.datetime64('2022-09-20T00:00:00.000000000'),
 numpy.datetime64('2022-09-21T00:00:00.000000000'),
 numpy.datetime64('2022-09-22T00:00:00.000000000'),
 numpy.datetime64('2022-09-23T00:00:00.000000000'),
 numpy.datetime64('2022-09-26T00:00:00.000000000'),
 numpy.datetime64('2022-09-27T00:00:00.000000000'),
 numpy.datetime64('2022-09-28T00:00:00.000000000'),
 numpy.datetime64('2022-09-29T00:00:00.000000000'),
 numpy.datetime64('2022-09-30T00:00:00.000000000'),
 numpy.datetime64('2022-10-03T00:00:00.000000000'),
 numpy.datetime64('2022-10-04T00:00:00.000000000'),
 numpy.datetime64('2022-10-05T00:00:00.000000000'),
 numpy.datetime64('2022-10-06T00:00:00.000000000'),
 numpy.datetime64('2022-10-07T00:00:00.000000000'),
 numpy.datetime64('2022-10-10T00:00:00.000000000'),
 numpy.datetime64('2022-10-11T00:00:00.000000000'),
 numpy.datetime64('2022-10-12T00:00:00.000000000'),
 numpy.datetime64('2022-10-13T00:00:00.000000000'),
 numpy.datetime64('2022-10-14T00:00:00.000000000'),
 numpy.datetime64('2022-10-17T00:00:00.000000000'),
 numpy.datetime64('2022-10-18T00:00:00.000000000'),
 numpy.datetime64('2022-10-19T00:00:00.000000000'),
 numpy.datetime64('2022-10-20T00:00:00.000000000'),
 numpy.datetime64('2022-10-21T00:00:00.000000000'),
 numpy.datetime64('2022-10-24T00:00:00.000000000'),
 numpy.datetime64('2022-10-25T00:00:00.000000000'),
 numpy.datetime64('2022-10-26T00:00:00.000000000'),
 numpy.datetime64('2022-10-27T00:00:00.000000000'),
 numpy.datetime64('2022-10-28T00:00:00.000000000'),
 numpy.datetime64('2022-10-31T00:00:00.000000000'),
 numpy.datetime64('2022-11-01T00:00:00.000000000'),
 numpy.datetime64('2022-11-02T00:00:00.000000000'),
 numpy.datetime64('2022-11-03T00:00:00.000000000'),
 numpy.datetime64('2022-11-04T00:00:00.000000000'),
 numpy.datetime64('2022-11-07T00:00:00.000000000'),
 numpy.datetime64('2022-11-08T00:00:00.000000000'),
 numpy.datetime64('2022-11-09T00:00:00.000000000'),
 numpy.datetime64('2022-11-10T00:00:00.000000000'),
 numpy.datetime64('2022-11-11T00:00:00.000000000'),
 numpy.datetime64('2022-11-14T00:00:00.000000000')]
   ,
   "Close": [347.559998,
 342.959991,
 340.769989,
 338.690002,
 345.299988,
 341.01001,
 337.25,
 341.059998,
 333.119995,
 338.029999,
 324.459991,
 310.600006,
 310.390015,
 306.839996,
 317.869995,
 322.809998,
 330.559998,
 329.820007,
 329.75,
 334.48999,
 333.73999,
 341.660004,
 334.899994,
 333.790009,
 325.450012,
 334.200012,
 330.450012,
 335.23999,
 346.179993,
 346.220001,
 342.940002,
 344.359985,
 336.350006,
 338.540009,
 336.529999,
 324.170013,
 332.459991,
 331.790009,
 328.070007,
 334.369995,
 333.26001,
 326.480011,
 331.899994,
 318.149994,
 319.589996,
 316.559998,
 303.170013,
 308.709991,
 300.149994,
 294.630005,
 294.640015,
 301.709991,
 313.26001,
 319.0,
 323.0,
 237.759995,
 237.089996,
 224.910004,
 220.179993,
 232.0,
 228.070007,
 219.550003,
 217.699997,
 221.0,
 216.539993,
 207.710007,
 206.160004,
 202.080002,
 198.449997,
 207.600006,
 210.479996,
 211.029999,
 203.490005,
 208.110001,
 202.970001,
 200.059998,
 187.470001,
 190.289993,
 198.5,
 195.210007,
 187.610001,
 186.630005,
 192.029999,
 203.630005,
 207.839996,
 216.490005,
 211.490005,
 216.649994,
 213.460007,
 219.570007,
 221.820007,
 223.589996,
 229.860001,
 227.850006,
 222.360001,
 224.850006,
 233.889999,
 231.839996,
 223.300003,
 222.949997,
 222.330002,
 216.460007,
 214.139999,
 214.990005,
 210.179993,
 210.770004,
 217.309998,
 200.419998,
 188.070007,
 184.110001,
 186.990005,
 180.949997,
 174.949997,
 205.729996,
 200.470001,
 211.130005,
 212.029999,
 223.410004,
 208.279999,
 203.770004,
 196.210007,
 197.649994,
 188.740005,
 191.240005,
 198.619995,
 200.039993,
 202.619995,
 192.240005,
 191.289993,
 193.539993,
 196.229996,
 181.279999,
 183.830002,
 191.630005,
 195.130005,
 193.639999,
 188.639999,
 198.860001,
 190.779999,
 194.25,
 195.649994,
 196.639999,
 184.0,
 175.570007,
 164.259995,
 163.729996,
 169.350006,
 160.869995,
 163.740005,
 157.050003,
 155.850006,
 158.75,
 170.160004,
 169.490005,
 160.679993,
 163.940002,
 161.25,
 160.029999,
 168.190002,
 169.770004,
 172.190002,
 170.880005,
 162.880005,
 163.270004,
 163.490005,
 158.050003,
 164.699997,
 167.229996,
 175.779999,
 183.089996,
 183.169998,
 169.270004,
 166.649994,
 159.149994,
 169.580002,
 160.720001,
 159.100006,
 159.929993,
 160.190002,
 168.800003,
 170.570007,
 167.110001,
 170.25,
 168.529999,
 178.339996,
 177.490005,
 180.5,
 180.889999,
 179.470001,
 174.850006,
 174.660004,
 167.960007,
 163.050003,
 161.110001,
 163.259995,
 168.779999,
 161.779999,
 159.169998,
 157.160004,
 162.929993,
 165.360001,
 160.320007,
 158.539993,
 160.389999,
 162.059998,
 169.149994,
 168.960007,
 153.130005,
 151.470001,
 149.550003,
 146.289993,
 148.020004,
 146.089996,
 142.119995,
 142.820007,
 140.410004,
 136.369995,
 134.399994,
 141.610001,
 136.410004,
 135.679993,
 138.610001,
 140.279999,
 138.979996,
 139.070007,
 133.449997,
 133.789993,
 128.539993,
 127.5,
 130.289993,
 126.760002,
 134.039993,
 132.800003,
 133.229996,
 131.529999,
 130.009995,
 129.720001,
 137.509995,
 129.820007,
 97.940002,
 99.199997,
 93.160004,
 95.199997,
 90.540001,
 88.910004,
 90.790001,
 96.720001,
 96.470001,
 101.470001,
 111.870003,
 113.019997,
 114.220001]
   ,
})