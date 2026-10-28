from playwright.sync_api import Page, expect
from config.settings import BASE_URL
from pages.base_page import BasePage


class ProductsPage(BasePage):
    URL = f"{BASE_URL}/products"

    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = self.page.get_by_role(
            "textbox", name="Search Product"
        )
        self.search_button = self.page.locator("#submit_search")

    def open(self) -> None:
        self.navigate(self.URL)

    def verify_products_page_loaded(self) -> None:
        expect(self.page).to_have_url(self.URL)
        expect(
            self.page.get_by_role("heading", name="All Products")
        ).to_be_visible()

    def search_product(self, product_name: str) -> None:
        self.search_input.fill(product_name)
        self.search_button.click()

    def verify_search_results(self) -> None:
        expect(
            self.page.get_by_role("heading", name="Searched Products")
        ).to_be_visible()

        products = self.page.locator(
            ".features_items .product-image-wrapper"
        )
        expect(products.first).to_be_visible()
        expect(products).not_to_have_count(0)

    def verify_no_search_results(self) -> None:
        expect(
            self.page.get_by_role("heading", name="Searched Products")
        ).to_be_visible()

        products = self.page.locator(
            ".features_items .product-image-wrapper"
        )
        expect(products).to_have_count(0)

    def add_product_to_cart(self, product_name: str) -> None:
        product_card = self.page.locator(
            ".features_items .product-image-wrapper"
        ).filter(
            has=self.page.locator(".productinfo p").get_by_text(
                product_name, exact=True
            )
        )

        expect(product_card).to_have_count(1)
        expect(product_card).to_be_visible()

        product_card.get_by_text(
            "Add to cart", exact=True
        ).first.click()
