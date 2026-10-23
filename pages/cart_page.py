
from playwright.sync_api import Page, expect

from config.settings import BASE_URL


class CartPage:
    URL = f"{BASE_URL}/view_cart"

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator("#cart_info")

    def open(self):
        self.page.goto(self.URL)

    def verify_cart_page_loaded(self):
        expect(self.page).to_have_url(self.URL)
        expect(self.cart_items).to_be_visible()

    def verify_product_in_cart(self, product_name: str):
        expect(
            self.cart_items.get_by_text(product_name, exact=True)
        ).to_be_visible()
