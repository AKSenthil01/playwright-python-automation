from pages.home_page import HomePage


def test_automationexercise_homepage_loads(page, base_url):
    home_page = HomePage(page)

    assert base_url.rstrip("/") in home_page.URL.rstrip("/")
    home_page.open()
    home_page.verify_homepage_loaded()
