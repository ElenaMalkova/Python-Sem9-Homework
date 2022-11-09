import pytest
from utils import convert_to_bin


def test_converter():
    assert convert_to_bin(42) == '101010'
    


