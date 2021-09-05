import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint
# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html"

driver.get(URL)

periodic_table_elements = driver.find_elements_by_xpath('//li[@class!="empty"]')

with open("periodic_data.txt", "r") as test_data:
    for index, row in enumerate(test_data.readlines()):
        row = row.split(", ")
        element_number = periodic_table_elements[index].get_attribute("data-pos")
        assert element_number == row[0]
        element_name = periodic_table_elements[index].find_element_by_tag_name("span").text
        assert element_name == row[1].replace("\n", "")