from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html"
driver.get(URL)

original_x_man = driver.find_element_by_xpath("/html/body/div/label[1]")
assert original_x_man.is_displayed()
original_x_man.click()
iceman = driver.find_element_by_xpath("//*[@id='iceman']/h2")


assert iceman.is_displayed()
assert not iceman.get_attribute("display")

x_factor = driver.find_element_by_xpath("/html/body/div/label[3]")
x_factor.click()

assert iceman.is_displayed()
assert not iceman.get_attribute("display")

x_force = driver.find_element_by_xpath("/html/body/div/label[2]")
x_force.click()

assert not iceman.is_displayed()


hellfire_club = driver.find_element_by_xpath("/html/body/div/label[4]")
hellfire_club.click()

assert not iceman.is_displayed()

driver.close()