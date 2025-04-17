import pytest

# test functions or test cases
@pytest.mark.smoke
def test_addition():
    n1 = 40
    n2 = 50
    assert n1+n2 == 90

@pytest.mark.smoke
def test_multiplication():
    n1 = 500
    n2 = 5
    assert n1*n2 == 2500

@pytest.mark.smoke
def test_division():
    n1 = 50
    n2 = 10
    assert n1//n2 == 5

@pytest.mark.sanity
def test_power_operation():
    n1 = 5
    assert n1**2 == 25


@pytest.mark.sanity
def test_subtraction():
    n1 = 500
    n2 = 600
    assert n2 - n1 == 100

@pytest.mark.smoke
@pytest.mark.sanity
def test_addition_fun1():
    n1 = 40
    n2 = 50
    assert n1+n2 == 90

@pytest.mark.regression
def test_multiplication_fun2():
    n1 = 500
    n2 = 5
    assert n1*n2 == 2500

@pytest.mark.regression
def test_division_fun3():
    n1 = 50
    n2 = 10
    assert n1//n2 == 5

@pytest.mark.regression
def test_power_operation_fun4():
    n1 = 5
    assert n1**2 == 25


@pytest.mark.regression
def test_subtraction_fun5():
    n1 = 500
    n2 = 600
    assert n2 - n1 == 100
