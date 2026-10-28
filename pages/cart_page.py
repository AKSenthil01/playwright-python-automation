from playwright.sync_api import Page, expect

from config.settings import BASE_URL
from pages.base_page import BasePage


class CartPage(BasePage):
    URL = f"{BASE_URL}/view_cart"

    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items = self.page.locator("#cart_info")

    def open(self) -> None:
        self.navigate(self.URL)

    def verify_cart_page_loaded(self) -> None:
        expect(self.page).to_have_url(self.URL)
        expect(self.cart_items).to_be_visible()

    def verify_product_in_cart(self, product_name: str) -> None:
        expect(
            self.cart_items.get_by_text(product_name, exact=True)
        ).to_be_visible()
