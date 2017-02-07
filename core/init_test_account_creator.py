from __future__ import absolute_import
import pytest
from core.pages import *
from tests import *

@pytest.mark.usefixtures("before_each_test")
class TestInitCreation():
    user_data = get_sing_in_user_data_for_positive_tests()

    @pytest.mark.parametrize("email, password", user_data)
    def test_sing_up_positive(self, email, password):
        SignInPopup.open_sign_up_popup()
        SingUpPopup.sign_up(email, password)
        FirstTimeLoggedPage.start_reading()
        LoggedUserPage.assert_user_logged_in(email)