import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html"

driver.get(URL)


def select(name, index):
    Select(driver.find_element_by_name(name)).select_by_index(index)

def fill_until_email():
    select("bf_totalGuests", 3)

    driver.find_element_by_xpath('//div[@id="step1"]//button').click()
    time.sleep(1)
    driver.find_element_by_name("bf_date").send_keys("1999")

    select("bf_time", 1)

    select("bf_hours", 1)

    driver.find_element_by_xpath('//div[@id="step2"]//button').click()
    time.sleep(1)

    driver.find_element_by_name("bf_fullname").send_keys("Tamas")

def fill_from_email():
    driver.find_element_by_name("bf_email").send_keys("t@t.hu")

    driver.find_element_by_xpath('//div[@id="step3"]//button').click()
    time.sleep(3)


#TC01:
fill_until_email()
fill_from_email()
message = "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."

displayed_message = driver.find_element_by_tag_name("h2").text
assert message == displayed_message

#TC02:
driver.get(URL)
time.sleep(2)
fill_until_email()

driver.find_element_by_name("bf_email").send_keys("tsfsdf")
driver.find_element_by_xpath('//div[@id="step3"]//button').click()
driver.find_element_by_name("bf_message").send_keys("bla")

assert driver.find_element_by_id("bf_email-error").is_displayed()