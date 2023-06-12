from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#spremanje nekog oglasa u "omiljene" na svom profilu
def test_add_to_favorites(login_process):
    wait = WebDriverWait(login_process, 10)
    sleep(5)
    random = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[2]/div[2]/div[3]/div[7]')))
    sleep(5)
    random.click()
    heart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/img')))
    heart.click()
    sleep(2)
    hamburger = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[1]/div[1]/div[2]/div/img[2]')))
    hamburger.click()
    saved = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[1]/div[3]/div[2]/div[2]/a[11]')))
    saved.click()
    message = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div/div/a/div/div[2]')))
    assert message.size != 0
    #nakon dodavanja provjerava se da li je prethodni oglas uspjesno spremljen u omiljene

#slanje poruke nekom korisniku
def test_send_message(login_process):
    wait = WebDriverWait(login_process, 10)
    messages = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/poruke"]')))
    messages.click()
    user = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(.,"Unknown192")]')))
    user.click()
    textarea = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[2]/div/textarea')))
    textarea.send_keys("KKS Seminarski :D")
    sleep(5)
    send = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[2]/div/div/button')))
    send.click()
    message = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(.,"KKS Seminarski :D")]'))) 
    sleep(5)
    assert message.size != 0
    #ako se poslana poruka prikaze u chat box-u onda se radi o uspjesnom slanju poruke

#kreiranje novog oglasa na profilu
def test_ad_posting(login_process):
    wait = WebDriverWait(login_process, 10)
    post = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/header/div/div[1]/div[2]/div/button')))
    post.click()
    category = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="modals-container"]/div/div/div[2]/div/div/div[2]/div/div[1]/div/button[3]')))
    category.click()
    subcategory = wait.until(EC.visibility_of_element_located((By.XPATH, '//label[contains(.,"Ostale usluge i servisi")]')))
    subcategory.click()
    value = wait.until(EC.visibility_of_element_located((By.XPATH, '//label[contains(.,"Servis bicikla")]')))
    value.click()
    title = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div[1]/div[2]/input')))
    title.send_keys("Test Oglas")
    sleep(5)
    continue_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[1]/div[5]/div/button')))
    continue_btn.click()
    sleep(5)
    publish_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/div[5]/div/button')))
    publish_btn.click()
    sleep(5)
    ad_list = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div/div/button')))
    ad_list.click()
    message = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div[1]/div/a')))
    assert message.size != 0
    #ako se novi oglas prikazuje u listi svih oglasa onda je dodavanje bilo uspjesno