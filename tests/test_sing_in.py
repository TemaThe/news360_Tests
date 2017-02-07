from __future__ import absolute_import
import pytest
from core.pages import *
from tests import old_user_data

@pytest.mark.usefixtures("before_each_test")
class TestSignIn():

    @pytest.mark.parametrize("email, password", old_user_data)
    def test_sing_in_positive(self, email, password):
        SignInPopup.sign_in(email, password)
        LoggedUserPage.assert_user_logged_in(email)



