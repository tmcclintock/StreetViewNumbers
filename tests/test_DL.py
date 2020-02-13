import StreetViewNumbers as SVN
import numpy as np
import numpy.testing as npt
import pytest

def test_DL():
    #Smoke test
    d = SVN.DataLoader()

def test_training_data():
    d = SVN.DataLoader()
    tx, ty = d.load_training_data()
    npt.assert_equal(4, len(tx.shape))
    npt.assert_equal(len(tx), len(ty))

def test_testing_data():
    d = SVN.DataLoader()
    tx, ty = d.load_testing_data()
    npt.assert_equal(4, len(tx.shape))
    npt.assert_equal(len(tx), len(ty))

