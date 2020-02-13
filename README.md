# StreetViewNumbers
Using AI to recognize address numbers.

## Insight data challenge

This repository is part of the Insight Data Challenge series, which has well-defined data science challenges that I am supposed to complete in less than six hours. For this project, I am using the [street view house numbers dataset](http://ufldl.stanford.edu/housenumbers/) (SVHN). For now, I will only be using the cropped, 32x32 centered-on-a-digit format (format 2 on the website).

## Installation

First install the requirements and then this project with

```bash
pip install -r requirements.txt
python setup.py install
``

The requirements are:

* [`numpy` and `scipy`](https://scipy.org/install.html)
* [`scikit-learn`](https://scikit-learn.org/stable/install.html)
* [`tensorflow`](https://www.tensorflow.org/install) >= version 2.0.0
* [`notebook`](https://jupyter.readthedocs.io/en/latest/install.html) (for running the example notebooks)
* [`matplotlib`](https://matplotlib.org/users/installing.html) (for notebooks)
* [`pytest`](https://docs.pytest.org/en/latest/getting-started.html) (for testing)

These can all be installed together using the `requirements.txt` file as shown above (assuming you have `pip`).

Once installed, test your installation with

```bash
pytest
```

If any tests fail, please raise an issue [here](https://github.com/tmcclintock/StreetViewNumbers/issues).

## Usage

TBD