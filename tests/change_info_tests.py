from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#promjena licnih informacija korisnika
def test_change_user_info(login_process):
    wait = WebDriverWait(login_process, 10)
    username = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/profil/ajdiinn01/aktivni"]')))
    username.click()
    settings_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[contains(.,"Postavke")]')))
    settings_btn.click()
    firstName = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/form/div[1]/input')))
    firstName.clear()
    firstName.send_keys("Ajdin")
    lastName = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/form/div[2]/input')))
    lastName.clear()
    lastName.send_keys("Bukvic")
    sleep(5)
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[contains(.,"Spasi izmjene")]')))
    save_btn.click()
    message = wait.until(EC.visibility_of_element_located((By.XPATH, '//p[contains(.,"Uspješno ste izmjenili profil.")]')))
    assert message.text == "Uspješno ste izmjenili profil."
    #kada se prikaze poruka za uspjeh znaci da su sve unesene promjene spremljene

#promjena lozinke s validnim podacima
def test_change_password_valid(login_process):
    wait = WebDriverWait(login_process, 10)
    username = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/profil/ajdiinn01/aktivni"]')))
    username.click()
    settings_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[contains(.,"Postavke")]')))
    settings_btn.click()
    change = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/mojolx/postavke/promjena-sifre"]')))
    change.click()
    oldPassword = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/input')))
    oldPassword.send_keys("seminarski999")
    newPassword = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/input')))
    newPassword.send_keys("12345678")
    newPasswordConfirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/input')))
    newPasswordConfirm.send_keys("12345678")
    sleep(2)
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[2]/div/button')))
    save_btn.click()
    message = wait.until(EC.visibility_of_element_located((By.XPATH, '//p[contains(.,"Uspješno ste izmijenili šifru.")]')))
    assert message.text == "Uspješno ste izmijenili šifru."
    #poruka uspjeha se prikazuje ako su uneseni validni podaci

#promjena lozinke s unesenim netacnim podacima
def test_change_password_wrong(login_process_ex):
    wait = WebDriverWait(login_process_ex, 10)
    username = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/profil/ajdiinn01/aktivni"]')))
    username.click()
    settings_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[contains(.,"Postavke")]')))
    settings_btn.click()
    change = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/mojolx/postavke/promjena-sifre"]')))
    change.click()
    oldPassword = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/input')))
    oldPassword.send_keys("test1234")
    newPassword = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/input')))
    newPassword.send_keys("12345678")
    newPasswordConfirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/input')))
    newPasswordConfirm.send_keys("12345678")
    sleep(2)
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[2]/div/button')))
    save_btn.click()
    message = wait.until(EC.visibility_of_element_located((By.XPATH, '//p[contains(.,"Stara šifra nije ispravna")]')))
    assert message.text == "Stara šifra nije ispravna"
    #poruka greske se prikazuje kada su uneseni podaci netacni
