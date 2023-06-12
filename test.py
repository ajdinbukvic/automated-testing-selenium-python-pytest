import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

#URL web aplikacije
PLANIKA = "https://planika.ba/"

#funkcija za setup chrome drivera i ostalih dodatnih opcija
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
    })
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options = options, service=service)
    driver.maximize_window()
    driver.get(PLANIKA)
    return driver

def test_pretraga(driver, capsys):       
    wait = WebDriverWait(driver, 10)
    pretraga_dugme = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="Pretraga"]')))
    pretraga_dugme.click()
    search_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='autocomplete']")))
    search_input.send_keys("cipele")
    search_input.send_keys(Keys.ENTER)
    rezultat = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='total-products-num']")))
    filter_dugme = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filtersList"]/div[1]/div/ul/li[1]/select'))))
    filter_dugme.select_by_index("2")
    filter_tekst = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="filtersList"]/div[1]/div/ul/li[1]/span/span[1]/span')))
    with capsys.disabled():
      print("Ukupno rezultata pretrage: " + rezultat.text)
      print("Ukljuceni filter za pretragu: " + filter_tekst.text)