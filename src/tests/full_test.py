import pytest

def test_basic():
    """
    Test that the data intensities are correct.
    """
    with open('data/dataaa.txt') as f:
        value = f.read()
    assert int(value) > 0


class TestClass:
    def test_otherintensities(self):
        """
        Test that the data intensities are correct.
        """
        with open('data/dataaa.txt') as f:
            value = f.read()
        assert int(value) < 0
    
    def test_otherintensities2(self):
        """
        Test that the data intensities are correct.
        """
        with open('data/dataaa.txt') as f:
            value = f.read()
        assert int(value) > 0