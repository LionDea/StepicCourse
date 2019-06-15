from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer") 
input1.send_keys(y)

#Checkbox
option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

# Radiobox
option2 = browser.find_element_by_id("robotsRule")
option2.click()

#Press button 
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)