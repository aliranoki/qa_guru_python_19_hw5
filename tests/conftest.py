import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene import browser


@pytest.fixture(scope="session")
def setup_browser():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")

    # Автоматическая установка ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 4.0

    yield browser
    browser.quit()