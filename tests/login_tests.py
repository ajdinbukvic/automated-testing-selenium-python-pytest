from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#funkcija za login u web aplikaciju s validnim podacima
def test_uspjesan_login(driver):       
    wait = WebDriverWait(driver, 10)
    login = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(.,"Prijavi se")]')))
    login.click()
    input_username = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
    input_username.send_keys("ajdiinn01")
    input_password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    input_password.send_keys("seminarski999")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Prijavi se")]')))
    login_button.click()
    username = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[contains(.,"ajdiinn01")]')))
    assert username.size != 0
    #ako se korisnik prebaci na pocetnu stranicu nakon unosa i pritiska dugmeta onda je login uspjesan 

#funkcija za login u web aplikaciju s netacnim podacima
def test_pogresan_pass(driver):
    wait = WebDriverWait(driver, 10)
    login = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(.,"Prijavi se")]')))
    login.click()
    input_username = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
    input_username.send_keys("ajdiinn01")
    input_password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    input_password.send_keys("pogresnasifra123")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Prijavi se")]')))
    login_button.click()
    error_message = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[contains(.,"Podaci nisu tačni.")]')))
    assert error_message.text == "Podaci nisu tačni."
    #ako se korisniku prikaze poruka greske onda znaci da uneseni podaci nisu validni