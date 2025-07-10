import pytest
from data_input import signup_list


@pytest.mark.parametrize( "username,password", [('XYZ', 'pass1'), ('DRE2', 'PASS2'), ('VBF3', 'PASS3')] )
def test_login_credential(username, password):
    print( "username:", username )
    print( "password:", password )


@pytest.mark.parametrize( "email,phone", signup_list )
def test_signup(email, phone):
    print( "email", email )
    print( "phone", phone )
