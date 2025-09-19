import pytest


@pytest.mark.smoke
def test_addition():
    n1 = 8
    n2 = 90
    assert n1 + n2 == 98


@pytest.mark.smoke
def test_multiplication():
    n1 = 8
    n2 = 90
    assert n1 * n2 == 720


@pytest.mark.smoke
def test_divison():
    n1 = 40
    n2 = 10
    assert n1 // n2 == 4


@pytest.mark.sanity
def test_subtraction():
    n1 = 98
    n2 = 90
    assert n1 - n2
