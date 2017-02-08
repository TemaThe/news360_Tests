# coding: utf-8
from __future__ import absolute_import
import pytest
from core.pages import *
from core.en_errors import *
from core.test_user_managment.test_data_generator import *


@pytest.mark.usefixtures("before_each_test")
class TestNegativeSignUp():


    def test_no_local_part_in_email(self):
        email = "@test.ru"
        password = "132435"
        SignInPopup.open_sign_up_popup()
        SingUpPopup.sign_up(email, password)
        SingUpPopup.assert_email_field_first_error_msg(THIS_VALUE_SHOULD_BE_A_VALID_EMAIL)


    def test_too_short_password(self):
        email = "test"+ get_str_timestamp() + "@test.ru"
        password = "12345"
        SignInPopup.open_sign_up_popup()
        SingUpPopup.sign_up(email, password)
        SingUpPopup.assert_password_field_first_error_msg(TOO_SHORT_PASSWORD)

    def test_already_created_email(self):
        users_data = get_static_sing_in_user_data_for_positive_tests()
        email = users_data[0][0]
        password = users_data[0][1]
        SignInPopup.open_sign_up_popup()
        SingUpPopup.sign_up(email, password)
        SingUpPopup.assert_top_error_msg()