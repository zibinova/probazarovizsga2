import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html"

driver.get(URL)

def guess(n):
    input_field = driver.find_element_by_tag_name("input")
    input_field.clear()
    input_field.send_keys(n)
    guess_button = driver.find_element_by_xpath('//*[@class="input-group-btn"]')
    guess_button.click()


def check_result():
    success_label = driver.find_element_by_xpath('//p[@ng-show="deviation === 0"]')
    if "ng-hide" not in success_label.get_attribute("class").split(" "):
        return True
    else:
        return False


num_of_guesses = 0


def find_secret_number():
    global num_of_guesses
    for i in range(1, 101):
        guess(i)
        num_of_guesses += 1
        if check_result():
            print("done")
            print(i)
            return i


num = find_secret_number()

#TC02

num_guesses_element = driver.find_element_by_xpath('//p[@class="text-info"]/span').text
assert num_of_guesses == int(num_guesses_element)
#TC01 positive

guess(num)
assert check_result()



#TC03
guess(-19)
guess(255)
num_guesses_element = driver.find_element_by_xpath('//p[@class="text-info"]/span').text
assert num_of_guesses + 3 == int(num_guesses_element)