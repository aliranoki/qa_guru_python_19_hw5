import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser


@pytest.fixture(scope="session")
def setup_browser():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    # Настройка Selene
    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 4.0  # Рекомендуется явно указать таймаут

    yield browser  # Фикстура возвращает объект browser для использования в тестах

    # Завершение работы после всех тестов
    browser.quit()