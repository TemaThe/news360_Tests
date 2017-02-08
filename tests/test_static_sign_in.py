from __future__ import absolute_import
import pytest
from core.pages import *
from core.test_user_managment.test_data_generator import *


@pytest.mark.usefixtures("before_each_test")
class TestSignIn():

    static_user_data = get_static_sing_in_user_data_for_positive_tests()

    @pytest.mark.parametrize("email, password", static_user_data)
    def test_sing_in_positive(self, email, password):
        SignInPopup.sign_in(email, password)
        LoggedUserPage.assert_user_logged_in(email)



