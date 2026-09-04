from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    # Переход на другую вкладку
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    # переключились на новую вкладку
    browser.switch_to.window(new_window)


    # Ваш код, который считывает значение Х и вычисляет значение У
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(str(y))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()