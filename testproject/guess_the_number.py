import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html"
driver.get(URL)

# fields defining:
restart_button = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/button")
guess_field = driver.find_element_by_xpath("/html/body/div/div[2]/input")
guess_button = driver.find_element_by_xpath("/html/body/div/div[2]/span/button")

restart_button.click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/input")))

guess_field.click()
guess_field.send_keys(random.randint(1, 100))
guess_button.click()

# while True:
# vegtelen ciklusban kell addig talalgatni amig ki nem talalja  prg a szamot, if feltetellel fole vagy ala menni
# ujra megadni a ranget a randomban stb.
