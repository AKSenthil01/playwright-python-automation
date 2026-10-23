from pages.products_page import ProductsPage


def test_search_for_nonexistent_product_returns_no_results(page):
    products_page = ProductsPage(page)

    products_page.open()
    products_page.search_product("NoSuchProductXYZ987")
    products_page.verify_no_search_results()
