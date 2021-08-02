import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"
driver.get(URL)
time.sleep(2)
movie_links = driver.find_elements_by_xpath("/html/body/div[2]/div[3]/a")

# validation of movies present
assert len(movie_links) == 24

# new movie entry:
# Film title: Black widow
# Release year: 2021
# Chronological year of events: 2020
# Trailer url: https://www.youtube.com/watch?v=Fp9pNPdNwjI
# Image url: https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg
# Film summary: https://www.imdb.com/title/tt3480822/

register_button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/button")
register_button.click()

# defining entry fields:

film_title = driver.find_element_by_id("nomeFilme")
release_year = driver.find_element_by_id("anoLancamentoFilme")
chronological_year = driver.find_element_by_id("anoCronologiaFilme")
trailer_url = driver.find_element_by_id("linkTrailerFilme")
image_url = driver.find_element_by_id("linkImagemFilme")
film_sum_url = driver.find_element_by_id("linkImdbFilme")

# test data:

test_data = ["Black Widow", "2021", "2020", "https://www.youtube.com/watch?v=Fp9pNPdNwjI",
             "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg",
             "https://www.imdb.com/title/tt3480822/"]

# filling register form
WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "nomeFilme")))

film_title.send_keys(test_data[0])
release_year.send_keys(test_data[1])
chronological_year.send_keys(test_data[2])
trailer_url.send_keys(test_data[3])
image_url.send_keys(test_data[4])
film_sum_url.send_keys(test_data[5])

save_button = driver.find_element_by_xpath("/html/body/div[2]/div[2]/fieldset/button[1]")
save_button.click()

movie_links = driver.find_elements_by_xpath("/html/body/div[2]/div[3]/a")

# validation of movies present
assert len(movie_links) == 25

driver.close()
