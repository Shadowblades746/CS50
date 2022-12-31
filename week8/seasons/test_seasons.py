import pytest
from seasons import format

def test_seasons():
    assert format("100") == "One hundred minutes"
