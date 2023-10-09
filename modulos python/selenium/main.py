from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

drive = Path(__file__).parent / 'drive' / 'geckodriver'

def make_browse():
    # para rodar sem interface '--headless'
    firefox_options = webdriver.FirefoxOptions()
    firefox_service = Service()# executable_path=drive
    browse = webdriver.Firefox(firefox_options, firefox_service)
    return browse

if __name__ == '__main__':
    browse = make_browse()
    browse.get('https://www.google.com.br/')
    input_google = WebDriverWait(browse, '10',).until(
        ec.presence_of_element_located(
            (By.NAME, 'q')
        )
    )

    input_google.send_keys('ola mundo')

    input_google.send_keys(Keys.ENTER)
    sleep(10)
    resultado = browse.find_element(By.ID, 'search')
    links = resultado.find_elements(By.TAG_NAME, 'a')
    links[0].click()
    browse.close()

