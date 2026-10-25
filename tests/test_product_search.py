
import json
from pathlib import Path

import pytest

from pages.products_page import ProductsPage


def load_product_search_data():
    data_file = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "product_search_data.json"
    )

    with data_file.open(encoding="utf-8") as file:
        return json.load(file)


@pytest.mark.regression
@pytest.mark.parametrize(
    "product_name",
    [
        item["product_name"]
        for item in load_product_search_data()
    ],
)
def test_search_product_returns_results(page, product_name):
    products_page = ProductsPage(page)

    products_page.open()
    products_page.search_product(product_name)
    products_page.verify_search_results()
