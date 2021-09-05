import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html"

driver.get(URL)
### prepare test data
characters = []
with open("characters.txt", "r") as chtest_data:
    for row in chtest_data.readlines():
        row = row.replace("\n", "")
        characters.append(row.split(","))


# pprint(characters)

# TestCase


def get_charcter_data(id):
    for character in characters:
        if character[0] == id:
            return character


character_elements = driver.find_elements_by_xpath('//ul[@class="characters"]/li')

for character_element in character_elements:
    id = character_element.get_attribute("id")
    teams = character_element.get_attribute("data-teams").split(" ")
    test_data = get_charcter_data(id)
    for team in test_data[1:]:
        assert team in teams

print("done")
