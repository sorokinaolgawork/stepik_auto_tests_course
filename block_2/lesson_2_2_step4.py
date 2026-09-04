from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
import time

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
