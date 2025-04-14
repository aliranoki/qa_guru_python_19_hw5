import pytest
from selene import browser
from selene.support.shared import config

@pytest.fixture(scope="session")
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'

    yield
    browser.quit()