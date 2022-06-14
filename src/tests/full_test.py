import pytest

def test_dataintensities():
    """
    Test that the data intensities are correct.
    """
    with open('data/dataaa.txt') as f:
        value = f.read()
    assert int(value) > 0