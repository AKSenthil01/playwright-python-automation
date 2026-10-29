import pytest

from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.regression
def test_products_page_loads(page):
    products_page = ProductsPage(page)

    products_page.open()
    products_page.verify_products_page_loaded()
