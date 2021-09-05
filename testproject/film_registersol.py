import csv

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"

driver.get(URL)

time.sleep(3)

### TC01

film_elements = driver.find_elements_by_xpath('//div[@class="container-total"]/a')

assert len(film_elements) == 24

### TC02

test_img = "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg"
test_title = "Black widow"
driver.find_element_by_xpath('//button[@class="mostra-container-cadastro"]').click()
time.sleep(2)
driver.find_element_by_id("nomeFilme").send_keys(test_title)
driver.find_element_by_id("anoLancamentoFilme").send_keys("2021")
driver.find_element_by_id("anoCronologiaFilme").send_keys("2020")
driver.find_element_by_id("linkTrailerFilme").send_keys("https://www.youtube.com/watch?v=Fp9pNPdNwjI")
driver.find_element_by_id("linkImagemFilme").send_keys(test_img)
driver.find_element_by_id("linkImdbFilme").send_keys("https://www.imdb.com/title/tt3480822/")

driver.find_element_by_xpath('//button[text()="Save"]').click()


film_elements = driver.find_elements_by_xpath(f'//h2[starts-with(text(),"{test_title}")]')

assert len(film_elements) == 1