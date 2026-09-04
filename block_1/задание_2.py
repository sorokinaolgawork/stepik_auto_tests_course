from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration(url):
    browser = webdriver.Chrome()
    try:
        browser.get(url)

        # проверка 
        print("URL:", browser.current_url)
        print("first:", len(browser.find_elements(By.CSS_SELECTOR, ".first_class input")))
        print("second:", len(browser.find_elements(By.CSS_SELECTOR, ".second_class input")))
        print("third:", len(browser.find_elements(By.CSS_SELECTOR, ".third_class input")))
        
        # Поля ввода
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_class input")
        first_name.send_keys("Ivan")
        
        last_name = browser.find_element(By.CSS_SELECTOR, ".second_class input")
        last_name.send_keys("Petrov")
        
        email = browser.find_element(By.CSS_SELECTOR, ".third_class input")
        email.send_keys("test@example.com")
        
        # Кнопка отправки
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Проверка успешной регистрации
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations!" in welcome_text, "Регистрация не удалась"
        
        return True
    finally:
        browser.quit()

# Запуск тестов
if __name__ == "__main__":
    # Должен пройти успешно
    test_registration("http://suninjuly.github.io/registration1.html")
    print("Тест на первой странице пройден")
    
    # Должен упасть с ошибкой NoSuchElementException
    test_registration("http://suninjuly.github.io/registration2.html")
    print("Тест на второй странице пройден")