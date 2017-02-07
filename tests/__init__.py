import pytest
from selene.tools import visit, get_driver, set_driver

from core.driver_manager import getChromeDriver
from core.pages import *
from core.test_data_generator import *


@pytest.fixture()
def before_each_test(request):
    setDriver()
    visit("https://news360.com/")
    MainPage.open_main_popup()
    MainPopup.open_sign_in_popup()

    def fin():
        get_driver().quit()
    request.addfinalizer(fin)

def setDriver():
    driver = getChromeDriver()
    driver.maximize_window()  # to read name from the top, else problem
    set_driver(driver)


new_user_data = get__sign_up_user_data_for_positive_tests()

old_user_data = get_sing_in_user_data_for_positive_tests()