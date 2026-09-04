# Вариант первый через try как и раньше

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



# try: 
#         browser = webdriver.Chrome()        
#         browser.get("http://suninjuly.github.io/explicit_wait2.html")

#         # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет цена 100$
#         waiting_price = WebDriverWait(browser, 12).until(
#                 EC.text_to_be_present_in_element((By.ID, "price"), "100")
#         )
#         button = browser.find_element(By.ID, "book")
#         button.click()

# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# Вариант второй через expected_conditions

browser = webdriver.Chrome()        
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет цена 100$
waiting_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
button = browser.find_element(By.ID, "book")
button.click()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)

button = browser.find_element(By.ID, "solve")
button.click()

alert = WebDriverWait(browser, 5).until(
    EC.alert_is_present()
)

print(alert.text)

browser.quit()
