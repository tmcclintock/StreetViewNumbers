import StreetViewNumbers as SVN
import numpy as np
import numpy.testing as npt
import pytest

def test_SVN():
    #Smoke test
    s = SVN.SVN()

def test_SVN_has_attr():
    s = SVN.SVN()
    npt.assert_equal(True, hasattr(s, "dims"))
