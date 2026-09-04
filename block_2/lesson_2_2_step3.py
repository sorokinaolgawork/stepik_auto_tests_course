from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который считывает значение Х и вычисляет значение У
    x1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x1 = x1_element.text
    x2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    x2 = x2_element.text
    y = int(x1) + int(x2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(y))



    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()