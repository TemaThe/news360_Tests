# coding: utf-8
import pytest
from selene.tools import visit, get_driver, set_driver
from core.driver_manager import getChromeDriver
from core.pages import *

@pytest.fixture
def before_each_test(request):
    open_sign_in_popup()

    def fin():
        get_driver().quit()
    request.addfinalizer(fin)


def open_sign_in_popup():
    setDriver()
    visit("https://news360.com/")
    MainPage.open_main_popup()
    MainPopup.open_sign_in_popup()


def setDriver():
    driver = getChromeDriver()
    driver.maximize_window()  # to read name from the top, else problem
    set_driver(driver)

