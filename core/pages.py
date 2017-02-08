# coding: utf-8
from selene.conditions import *
from selene.tools import s, ss

from core.en_errors import *


class MainPage:

    START_READING_BUTTON = s(".startreading")
    CHANGE_LANGUAGE_BUTTON = s("[ng-bind='::localization.lang']")
    EN_LANGUAGE_BUTTON = s("[v='en']")
    DE_LANGUAGE_BUTTON = s("[v='de']")

    @classmethod
    def open_main_popup(cls):
        cls.START_READING_BUTTON.click()





class MainPopup():
    SIGN_WITH_EMAIL_LINK = s(".simplepopup .bHSignIn .login-signin")
    CLOSE_CROSS = s(".close")

    #CAN BE USED TO CHECK THIS POPUP - NOT IMPLEMENTED IN TEST SETS
    WELCOME_MESSAGE = s(".simplepopup [ng-bind='::localization.landing_great']")
    CREATE_MESSAGE = s(".simplepopup [ng-bind='::localization.landing_personalize_newsfeed_text']")
    AND_PASSWORD_TEXT = s(".simplepopup [ng-bind='::localization.landing_sign_in_password']")

    @classmethod
    def open_sign_in_popup(cls):
        cls.SIGN_WITH_EMAIL_LINK.click()






class SignInPopup():
    EMAIL_FIELD = s(".simplepopup .bHSignIn .signin .email")
    PASSWORD_FIELD = s(".simplepopup .bHSignIn .signin .password")

    UPPER_ERROR_COMMENT = s(".simplepopup .bHSignIn .error-message")
    EMAIL_FIELD_ERROR_COMMENT_LIST = ss(".simplepopup .bHSignIn .singin .email + ul")
    PASSWORD_FIELD_ERROR_COMMENT_LIST = ss(".simplepopup .bHSignIn .singin .password + ul")

    FORGOT_PASSWORD_LINK = s(".simplepopup .bHSignIn .signin .forgotpass")
    SING_UP_LINK = s(".simplepopup .bHSignIn .signin .signup")

    CANCEL_BUTTON = s(".simplepopup .bHSignIn .signin .cancel-button")
    SING_IN_BUTTON = s(".simplepopup .bHSignIn .signin .signin-button")

    @classmethod
    def sign_in(cls, email, password):
        cls.EMAIL_FIELD.set(email)
        cls.PASSWORD_FIELD.set(password)
        cls.SING_IN_BUTTON.click()

    @classmethod
    def open_sign_up_popup(cls):
        cls.SING_UP_LINK.click()

    @classmethod
    def assert_top_error_msg(cls):
        cls.UPPER_ERROR_COMMENT.should_be(exact_text(INVALID_LOGIN_OR_PASSWORD_EN))





class SingUpPopup():
    EMAIL_FIELD = s(".simplepopup .bHSignIn .signup .email")
    PASSWORD_FIELD = s(".simplepopup .bHSignIn .signup .password")
    CONFIRM_PASSWORD_FIELD = s(".simplepopup .bHSignIn .signup .confirmpassword")

    UPPER_ERROR_COMMENT = s(".simplepopup .bHSignIn .error-message")
    EMAIL_FIELD_ERROR_COMMENT_LIST = ss(".simplepopup .bHSignIn .signup .email + ul li")
    PASSWORD_FIELD_ERROR_COMMENT_LIST = ss(".simplepopup .bHSignIn .signup .password + ul")
    CONFIRM_PASSWORD_FIELD_ERROR_COMMENT_LIST = s(".simplepopup .bHSignIn .signup .confirmpassword + ul")

    LOG_IN_LINK = s(".simplepopup .bHSignIn .signup .login")

    CANCEL_BUTTON = s(".simplepopup .bHSignIn .signup .cancel-button")
    SING_UP_BUTTON = s(".simplepopup .bHSignIn .signup .signup-button")

    @classmethod
    def sign_up(cls, email, password):
        cls.EMAIL_FIELD.set(email)
        cls.PASSWORD_FIELD.set(password)
        cls.CONFIRM_PASSWORD_FIELD.set(password)
        cls.SING_UP_BUTTON.click()

    @classmethod
    def assert_top_error_msg(cls):
        cls.UPPER_ERROR_COMMENT.should_be(exact_text(INVALID_LOGIN_OR_PASSWORD))

    @classmethod
    def assert_email_field_first_error_msg(cls, text):
        cls.EMAIL_FIELD_ERROR_COMMENT_LIST.first().should_be(exact_text(text))

    @classmethod
    def assert_email_field_second_error_msg(cls, text):
        cls.EMAIL_FIELD_ERROR_COMMENT_LIST.index(1).should_be(exact_text(text))

    @classmethod
    def assert_password_field_first_error_msg(cls, text):
        cls.PASSWORD_FIELD_ERROR_COMMENT_LIST.first().should_be(exact_text(text))

    @classmethod
    def assert_password_field_second_error_msg(cls, text):
        cls.PASSWORD_FIELD_ERROR_COMMENT_LIST.index(1).should_be(exact_text(text))




class ResetPasswordPopup():
    EMAIL_FIELD = s(".simplepopup .bHSignIn .resetpassword .email")

    LOG_IN_LINK = s(".simplepopup .bHSignIn .resetpassword .login")
    SING_UP_LINK = s(".simplepopup .bHSignIn .resetpassword .signup")

    RESET_PASSWORD_BUTTON = s(".simplepopup .bHSignIn .resetpassword .reset-button")





class LoggedUserPage():
    LOGO = s(".logo")
    USERNAME = s(".username")
    SETTINGS_LINK = s(".user")

    @classmethod
    def assert_user_logged_in(cls, email):
        cls.LOGO.should_be(visible, timeout=20)

    @classmethod
    def open_settings(cls):
        cls.SETTINGS_LINK.click()

    @classmethod
    def assert_right_user_logged_in(cls, email):
        name = email.rpartition('@')[0].upper()
        cls.USERNAME.should_have(exact_text(name), timeout=5)




class SettingsPage():
    LOGOUT = s(".logout")

    @classmethod
    def logout(cls):
        cls.LOGOUT.click()




class FirstTimeLoggedPage():
    START_READING = s(".startReading")

    @classmethod
    def start_reading(cls):
        cls.START_READING.insist(condition=clickable, timeout=1)
        cls.START_READING.insist(condition=visible, timeout=1)
        cls.START_READING.hover().click()
