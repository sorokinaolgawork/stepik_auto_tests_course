import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistration(unittest.TestCase):
    
    def test_reg1(self):
        # Тест для первой (рабочей) страницы
        browser = webdriver.Chrome()
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)

            # Заполняем только обязательные поля (те, что с красной звездочкой)
            # Используем CSS-селекторы по уникальным классам полей
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            input3.send_keys("ivan@example.com")

            # Отправляем форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Ждем загрузки страницы приветствия
            time.sleep(1)

            # Находим элемент с текстом успешной регистрации
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            # Проверяем, что текст совпадает с ожидаемым
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
            
        finally:
            browser.quit()

    def test_reg2(self):
        # Тест для второй (сломанной) страницы
        browser = webdriver.Chrome()
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)

            # Код поиска элементов такой же, как в первом тесте
            # На этой странице он упадет с ошибкой NoSuchElementException
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            input3.send_keys("ivan@example.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
            
        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()
