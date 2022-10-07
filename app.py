import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import pyautogui
import pyperclip

import sys


def get_programme():
    path = sys.argv[1]
    with open(path, 'r') as file:
        data = file.read()

    return data


def launch_programme():
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome("./chromedriver", options=options)

    driver.get('https://algoscript.info/')

    time.sleep(0.3)  # Let the user actually see something!
    driver.switch_to.alert.accept()

    time.sleep(0.3)

    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.click()
    time.sleep(0.1)
    pyautogui.hotkey("ctrl", "v")

    time.sleep(0.2)
    driver.find_element(By.XPATH, '//*[@id="icoExec"]').click()

    dropdown = Select(driver.find_element(By.XPATH, '//*[@id="titre_onglet"]'))
    time.sleep(0.2)
    dropdown.select_by_index(2)


if __name__ == '__main__':
    paperclip = pyperclip.paste()

    prog = get_programme()
    pyperclip.copy(prog)
    launch_programme()

    pyperclip.copy(paperclip)
