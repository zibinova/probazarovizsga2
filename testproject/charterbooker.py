import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html"
driver.get(URL)
time.sleep(1)
select = Select(driver.find_element_by_name("bf_totalGuests"))
select.select_by_value("5")

next_button = driver.find_element_by_xpath("//*[@id='step1']/ul/li[2]/button")
next_button.click()

datepicker_field = driver.find_element_by_xpath("//input[@class='datepicker']")
datepicker_field.send_keys("8/2/2021 12:05")

select = Select(driver.find_element_by_name("bf_time"))
select.select_by_value("Midday")

select = Select(driver.find_element_by_name("bf_hours"))
select.select_by_value("3")

# redefine next button
next_button = driver.find_element_by_xpath("//*[@id='step2']/ul/li[4]/button")
next_button.click()

name_field = driver.find_element_by_xpath("//input[@name='bf_fullname']")
name_field.send_keys("J Lo")

email_field = driver.find_element_by_xpath("//input[@name='bf_email']")
email = "jlo@jlo.hu"
email_field.send_keys(email)
# assert email

submit_button = driver.find_element_by_class_name("submit-btn")
submit_button.click()
time.sleep(2)
confirmation = driver.find_element_by_xpath("//*[@id='booking-form']/h2")
confirmation_text = "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning ' \
                                              '(Unless we're sailing or eating tacos!)."

assert driver.find_element_by_xpath("//*[@id='booking-form']/h2").text() == confirmation_text



# 11 pont / az assert-hez alkalmazott szövegben van egy sortörés; nincs email validációd