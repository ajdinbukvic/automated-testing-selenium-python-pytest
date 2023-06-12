from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#pretraga oglasa po kategoriji
def test_search_by_category(driver):
    wait = WebDriverWait(driver, 10)
    category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/kategorije"]')))
    category_btn.click()
    cars_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/pretraga?category_id=18"]')))
    cars_btn.click()
    cars_list = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]')))
    assert cars_list.text == "Automobili"
    #provjera da li se nakon pretrage prikazuju oglasi koji pripadaju kategoriji automobili

#pretraga oglasa prema unesenoj kljucnoj rijeci
def test_search_by_key_word(driver):
    wait = WebDriverWait(driver, 10)
    search = wait.until(EC.element_to_be_clickable((By.NAME, "notASearchField")))
    search.send_keys("audi a6")
    search.send_keys(Keys.ENTER)
    search_results = wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[contains(.,"Audi A6")]')))
    assert search_results.size != 0
    #pretraga je uspjesno ako postoje rezultati pretrage koji zadovoljavaju unesenu vrijednost

#pretraga oglasa na osnovu filtriranja razlicitih opcija
def test_search_by_filter(driver):
    wait = WebDriverWait(driver, 10)
    category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/vozila"]')))
    category_btn.click()
    price_lower = wait.until(EC.element_to_be_clickable((By.ID, "price_lower")))
    price_lower.send_keys("20000")
    price_upper = wait.until(EC.element_to_be_clickable((By.ID, "price_upper")))
    price_upper.send_keys("30000")
    location = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div/div[2]/div/select'))))
    location.select_by_value("4")
    search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/button')))
    search.click()
    results = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(.,"28.000 KM")]')))
    assert results.size != 0
    #ako postoji neki element koji zadovoljava uslove filtriranja pretraga je uspjesna