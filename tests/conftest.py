import pytest
from selene import browser
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture(scope="session")
def setup_browser():
    # Настройка ChromeDriver через WebDriver Manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'

    yield
    browser.quit()