
import pytest

from pages.products_page import ProductsPage


@pytest.mark.parametrize(
    "product_name",
    [
        "NoSuchProductXYZ987",
        "UnknownItemABC123",
    ],
)
def test_search_for_nonexistent_product_returns_no_results(
    page, product_name
):
    products_page = ProductsPage(page)

    products_page.open()
    products_page.search_product(product_name)
    products_page.verify_no_search_results()
