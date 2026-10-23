from playwright.sync_api import Page, expect
from config.settings import BASE_URL


class HomePage:
    URL = f"{BASE_URL}/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def verify_homepage_loaded(self):
        expect(self.page).to_have_title("Automation Exercise")
