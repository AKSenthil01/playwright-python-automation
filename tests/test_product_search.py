from pages.products_page import ProductsPage


def test_search_product_returns_results(page):
    products_page = ProductsPage(page)

    products_page.open()
    products_page.search_product("Blue Top")
    products_page.verify_search_results()
