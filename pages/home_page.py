from playwright.sync_api import expect
from config.settings import BASE_URL
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = f"{BASE_URL}/"

    def open(self) -> None:
        self.navigate(self.URL)

    def verify_homepage_loaded(self) -> None:
        expect(self.page).to_have_title("Automation Exercise")
