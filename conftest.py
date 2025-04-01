import pytest
from selene import browser
from selene.support.shared import config

@pytest.fixture(scope="session")
def setup_browser():
    # Настройка конфигурации браузера
    config.window_width = 1920
    config.window_height = 1080
    config.base_url = 'https://demoqa.com'

    yield
    browser.quit()