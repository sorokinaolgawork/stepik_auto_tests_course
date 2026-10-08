import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestNew(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("test_123@test.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки страницы
        time.sleep(1)

        # Получаем текст заголовка
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # Проверяем результат
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text
        )

        browser.quit()

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("test_123@test.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки страницы
        time.sleep(1)

        # Получаем текст заголовка
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # Проверяем результат
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text
        )

        browser.quit()


if __name__ == "__main__":
    unittest.main()