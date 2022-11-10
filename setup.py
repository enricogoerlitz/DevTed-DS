from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "1.0.0"
DESCRIPTION = "Data Gathering/Visualization/Cleaning/Preprocessing. Database connection & query execution. Machine Learning."
LONG_DESCRIPTION = "A package that helps to get, visualize, clean and preprocess data for analysing and machine learning."
REQUIREMENTS = [
    "numpy",
    "pandas",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "xgboost",
    "missongno",
    "imblearn",
]

# Setting up
setup(
    name="devted",
    version=VERSION,
    author="CoolerTeddy (Enrico Goerlitz)",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    keywords=["python", "data", "data science", "data analysis", "machine learning", "database"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
