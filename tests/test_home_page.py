
import pytest

from pages.home_page import HomePage


@pytest.mark.smoke
def test_automationexercise_homepage_loads(page, base_url):
    home_page = HomePage(page)
    assert home_page.URL.rstrip("/") == base_url.rstrip("/")
    home_page.open()
    home_page.verify_homepage_loaded()
