
import re

import pytest
from playwright.sync_api import Page, expect

from pages.playwright_docs_page import PlaywrightDocsPage


def test_homepage_has_expected_title(page: Page):
    docs_page = PlaywrightDocsPage(page)

    docs_page.open_homepage()
    docs_page.verify_homepage_title()


def test_homepage_displays_get_started_link(page: Page):
    docs_page = PlaywrightDocsPage(page)

    docs_page.open_homepage()
    docs_page.verify_get_started_link_visible()


def test_get_started_navigation(page: Page):
    docs_page = PlaywrightDocsPage(page)

    docs_page.open_homepage()
    docs_page.click_get_started()

    expect(page).to_have_url(
        "https://playwright.dev/docs/intro"
    )
    expect(page).to_have_title(re.compile("Playwright"))
    expect(
        page.get_by_role("heading", name="Installation")
    ).to_be_visible()


@pytest.mark.parametrize(
    "path, expected_heading",
    [
        ("/docs/intro", "Installation"),
        ("/docs/writing-tests", "Writing tests"),
    ],
)
def test_documentation_pages(
    page: Page,
    path: str,
    expected_heading: str,
):
    docs_page = PlaywrightDocsPage(page)
    docs_page.open_documentation_page(path)

    expect(
        page.get_by_role("heading", name=expected_heading).first
    ).to_be_visible()
