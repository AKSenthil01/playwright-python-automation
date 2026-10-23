from playwright.sync_api import Page, expect
from config.settings import BASE_URL


class ProductsPage:
    URL = f"{BASE_URL}/products"

    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_role(
            "textbox", name="Search Product"
        )
        self.search_button = page.locator("#submit_search")

    def open(self):
        self.page.goto(self.URL)

    def verify_products_page_loaded(self):
        expect(self.page).to_have_url(self.URL)
        expect(
            self.page.get_by_role("heading", name="All Products")
        ).to_be_visible()

    def search_product(self, product_name: str):
        self.search_input.fill(product_name)
        self.search_button.click()

    def verify_search_results(self):
        expect(
            self.page.get_by_role("heading", name="Searched Products")
        ).to_be_visible()

        products = self.page.locator(
            ".features_items .product-image-wrapper"
        )
        expect(products.first).to_be_visible()
        assert products.count() > 0, "No products were returned by search"

    def verify_no_search_results(self):
        expect(
            self.page.get_by_role(
                "heading", name="Searched Products"
            )
        ).to_be_visible()

        products = self.page.locator(
            ".features_items .product-image-wrapper"
        )
        expect(products).to_have_count(0)

    def add_product_to_cart(self, product_name: str):
        product_card = self.page.locator(
            ".features_items .product-image-wrapper"
        ).filter(
            has=self.page.locator(".productinfo p").get_by_text(
                product_name, exact=True
            )
        ).first

        expect(product_card).to_be_visible()
        product_card.get_by_text(
            "Add to cart", exact=True
        ).first.click()
