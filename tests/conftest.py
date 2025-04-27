import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selene import browser


@pytest.fixture(scope="session")
def setup_browser():
    # Настройка опций Chrome
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")  # Обход ограничений для Linux
    chrome_options.add_argument("--disable-dev-shm-usage")  # Для ограниченных ресурсов
    chrome_options.add_argument("--headless")  # Режим без графического интерфейса

    # Указываем путь к ChromeDriver (предполагается, что он установлен в /usr/local/bin/)
    service = Service(executable_path='/usr/local/bin/chromedriver')

    # Инициализация драйвера
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Настройка Selene
    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 4.0  # Рекомендуется явно указать таймаут

    yield browser  # Фикстура возвращает объект browser для использования в тестах

    # Завершение работы после всех тестов
    browser.quit()