from selene.conditions import *
from selene.tools import s

class MainPage:

    START_READING_BUTTON = s(".startreading")
    CHANGE_LANGUAGE_BUTTON = s("[ng-bind='::localization.lang']")
    EN_LANGUAGE_BUTTON = s("[v='en']")
    DE_LANGUAGE_BUTTON = s("[v='de']")

    @classmethod
    def openMainCreateAccountPopup(cls):
        cls.START_READING_BUTTON.click()


class MainCreateAccountPopup():
    SIGN_WITH_EMAIL_LINK = s(".simplepopup .bHSignIn .login-signin")
    CLOSE_CROSS = s(".close")

    #CAN BE USED TO CHECK THIS POPUP - NOT IMPLEMENTED IN TEST SETS
    WELCOME_MESSAGE = s(".simplepopup [ng-bind='::localization.landing_great']")
    CREATE_MESSAGE = s(".simplepopup [ng-bind='::localization.landing_personalize_newsfeed_text']")
    AND_PASSWORD_TEXT = s(".simplepopup [ng-bind='::localization.landing_sign_in_password']")

    @classmethod
    def openSingIN_WithEmailPopup(cls):
        cls.SIGN_WITH_EMAIL_LINK.click()



class SingIN_WithEmailPopup():
    EMAIL_FIELD = s(".simplepopup .bHSignIn .signin .email")
    PASSWORD_FIELD = s(".simplepopup .bHSignIn .signin .password")

    UPPER_ERROR_COMMENT = s(".simplepopup .bHSignIn .error-message")
    EMAIL_FIELD_ERROR_COMMENT_LIST = s(".simplepopup .bHSignIn .singin .email + ul")
    PASSWORD_FIELD_ERROR_COMMENT_LIST = s(".simplepopup .bHSignIn .singin .password + ul")

    FORGOT_PASSWORD_LINK = s(".simplepopup .bHSignIn .signin .forgotpass")
    SING_UP_LINK = s(".simplepopup .bHSignIn .signin .signup")

    CANCEL_BUTTON = s(".simplepopup .bHSignIn .signin .cancel-button")
    SING_IN_BUTTON = s(".simplepopup .bHSignIn .signin .signin-button")

    @classmethod
    def signIn(cls, email, password):
        cls.EMAIL_FIELD.set(email)
        cls.PASSWORD_FIELD.set(password)
        cls.SING_IN_BUTTON.click()

    @classmethod
    def openSingUP_WithEmailPopup(cls):
        cls.SING_UP_LINK.click()


class SingUP_WithEmailPopup():
    EMAIL_FIELD = s(".simplepopup .bHSignIn .signup .email")
    PASSWORD_FIELD = s(".simplepopup .bHSignIn .signup .password")
    CONFIRM_PASSWORD_FIELD = s(".simplepopup .bHSignIn .signup .confirmpassword")

    UPPER_ERROR_COMMENT = s(".simplepopup .bHSignIn .error-message")
    EMAIL_FIELD_ERROR_COMMENT_LIST = s(".simplepopup .bHSignIn .signup .email + ul")
    PASSWORD_FIELD_ERROR_COMMENT_LIST = s(".simplepopup .bHSignIn .signup .password + ul")
    CONFIRM_PASSWORD_FIELD_ERROR_COMMENT_LIST = s(".simplepopup .bHSignIn .signup .confirmpassword + ul")

    LOG_IN_LINK = s(".simplepopup .bHSignIn .signup .login")

    CANCEL_BUTTON = s(".simplepopup .bHSignIn .signup .cancel-button")
    SING_UP_BUTTON = s(".simplepopup .bHSignIn .signup .signup-button")

    @classmethod
    def signUp(cls, email, password):
        cls.EMAIL_FIELD.set(email)
        cls.PASSWORD_FIELD.set(password)
        cls.CONFIRM_PASSWORD_FIELD.set(password)
        cls.SING_UP_BUTTON.click()



class ResetPasswordPopup():
    EMAIL_FIELD = s(".simplepopup .bHSignIn .resetpassword .email")

    LOG_IN_LINK = s(".simplepopup .bHSignIn .resetpassword .login")
    SING_UP_LINK = s(".simplepopup .bHSignIn .resetpassword .signup")

    RESET_PASSWORD_BUTTON = s(".simplepopup .bHSignIn .resetpassword .reset-button")

class MainLoggedInUserPage():
    LOGO = s(".logo")
    USERNAME = s(".username")

    @classmethod
    def checkPageLoaded(cls, email):
        cls.LOGO.should_be(visible, timeout=20)
        name = cls.getNameFromEmail(email)
        cls.USERNAME.should_have(exact_text(name), timeout=5)

    @classmethod
    def getNameFromEmail(cls, email):
        return email.rpartition('@')[0].upper()



class JustSingedUPUserPage():
    START_READING = s(".startReading")

    @classmethod
    def startReading(cls):
        cls.START_READING.insist(condition=clickable, timeout=15)
        cls.START_READING.insist(condition=visible, timeout=15)
        cls.START_READING.hover().click()
