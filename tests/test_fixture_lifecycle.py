
def test_first_page_has_expected_url(page, base_url):
    page.goto(base_url, wait_until="domcontentloaded")
    assert page.url.startswith(base_url)


def test_second_page_starts_independently(page, base_url):
    # This test receives its own page fixture.
    assert page.url == "about:blank"

    page.goto(base_url, wait_until="domcontentloaded")
    assert page.url.startswith(base_url)
