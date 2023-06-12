import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#URL web aplikacije
OLX = "https://olx.ba"

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
    driver.get(OLX)
    return driver

#funkcija koja sluzi za login u web aplikaciju i pokrece se prije svakog pojedinacnog testa
@pytest.fixture
def login_process(driver):          
    wait = WebDriverWait(driver, 10)
    login = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(.,"Prijavi se")]')))
    login.click()
    input_username = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
    input_username.send_keys("ajdiinn01")
    input_password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    input_password.send_keys("seminarski999")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Prijavi se")]')))
    login_button.click()
    wait.until(EC.invisibility_of_element((By.NAME, "username")))
    wait.until(EC.invisibility_of_element((By.NAME, "password")))
    return driver

#funkcija koja sluzi za login u web aplikaciju i pokrece se prije svakog pojedinacnog testa
@pytest.fixture
def login_process_ex(driver):          
    wait = WebDriverWait(driver, 10)
    login = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(.,"Prijavi se")]')))
    login.click()
    input_username = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
    input_username.send_keys("ajdiinn01")
    input_password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    input_password.send_keys("12345678")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Prijavi se")]')))
    login_button.click()
    wait.until(EC.invisibility_of_element((By.NAME, "username")))
    wait.until(EC.invisibility_of_element((By.NAME, "password")))
    return driver
