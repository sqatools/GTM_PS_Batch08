import pytest
"""
Fixture function scope:
function scope :  function scope fixture will execute before and after execution of each test cases.
class scope : class fixture will execute before and after execution of each test case.
module scope : Module scope fixture will execute before and after execution of entire module test cases.
package scope : Package  scope fixture will execute before and after execution of all the modules in the package.
session scope : Session scope fixture will execute once session is started and completed once the session is 
                completed.


"""

@pytest.fixture(scope="function", autouse=True)
def setup():
    print("\n -- function execution started --")
    yield

    print("\n -- function execution completed --")

@pytest.fixture(scope="module", autouse=True)
def module_setup():
    print("\n -- module execution started --")
    yield

    print("\n -- module execution completed --")

@pytest.fixture(scope="package", autouse=True)
def package_setup():
    print("\n -- package execution started --")
    yield

    print("\n -- package execution completed --")


@pytest.fixture(scope="session", autouse=True)
def session_setup():
    print("\n -- session execution started --")
    yield

    print("\n -- session execution completed --")

def test_addition():
    n1 = 40
    n2 = 50
    assert n1 + n2 == 90


def test_multiplication():
    n1 = 500
    n2 = 5
    assert n1 * n2 == 2500


def test_division():
    n1 = 50
    n2 = 10
    assert n1 // n2 == 50
