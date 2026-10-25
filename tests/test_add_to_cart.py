
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.products_page import ProductsPage


def test_add_product_to_cart(page):
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    products_page.open()

    with page.expect_response(
            lambda response: (
                    "/add_to_cart/1" in response.url
                    and response.request.method == "GET"
            )
    ) as response_info:
        products_page.add_product_to_cart("Blue Top")

    response = response_info.value
    assert response.status == 200, (
        f"Add-to-cart request failed: HTTP {response.status}"
    )

    # Verify the add-to-cart confirmation.
    expect(page.get_by_text("Added!", exact=True)).to_be_visible()

    # Navigate to the cart and verify its contents.
    page.get_by_text("View Cart", exact=True).click()

    cart_page.verify_cart_page_loaded()
    cart_page.verify_product_in_cart("Blue Top")
