# coding: utf-8
import os
from sys import platform as _platform
from selenium import webdriver

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DRIVERS_DIR = os.path.join(CURRENT_DIR, 'drivers')

WIN_CHROME_DRIVER = os.path.join(DRIVERS_DIR, 'chromedriver.exe')
MAC_CHROME_DRIVER = os.path.join(DRIVERS_DIR, 'chromedriver')

def getChromeDriver():
    if _platform == "darwin":
        path = MAC_CHROME_DRIVER
    else:
        path = WIN_CHROME_DRIVER
    driver = webdriver.Chrome(executable_path=path)
    return driver