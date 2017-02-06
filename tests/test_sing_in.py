from __future__ import absolute_import
from unittest import TestCase
from selene.tools import visit


from core.driver_manager import getChromeDriver
from core.locators import *
import time
from selene.tools import set_driver, get_driver

class Test_Exchange_Manager(TestCase):

    def setUp(self):
        print "Test ", self._testMethodName
        self.setDriver()
        visit("https://news360.com/")
        MainPage.openMainCreateAccountPopup()
        MainCreateAccountPopup.openSingIN_WithEmailPopup()

    def setDriver(self):
        driver = getChromeDriver()
        set_driver(driver)

    def tearDown(self):
        get_driver().quit()

    def test_sing_in_positive(self):
        email = 'temamod@gmail.com'
        password = '132435'
        SingIN_WithEmailPopup.signIn(email, password)
        MainLoggedInUserPage.checkPageLoaded(email)

    def test_sing_up_positive(self):
        timestamp = str(time.time())
        email = 'testASM' + timestamp +'@gmail.com'
        password = '132435'

        SingIN_WithEmailPopup.openSingUP_WithEmailPopup()
        SingUP_WithEmailPopup.signUp(email, password)
        JustSingedUPUserPage.startReading()
        MainLoggedInUserPage.checkPageLoaded(email)

