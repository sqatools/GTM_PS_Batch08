import pytest
from data_inputs import signup_list

@pytest.mark.parametrize("username, password",[('user1', 'pass1'), ('user2', 'password2'), ('user3', 'pass3')])
def test_login(username, password):
    print("username :", username)
    print("password :", password)


@pytest.mark.parametrize("email, phone", signup_list)
def test_signup(email, phone):
    print("email :", email)
    print("phone :", phone)

