
from playwright.sync_api import Page, expect


def test_homepage_has_expected_title(page: Page):
    page.goto("https://playwright.dev/")

    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")


def test_homepage_displays_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    expect(
        page.get_by_role("link", name="Get started")
    ).to_be_visible()


def test_get_started_navigation(page: Page):
    page.goto("https://playwright.dev/")

    page.get_by_role("link", name="Get started").click()

    expect(page).to_have_url(
        "https://playwright.dev/docs/intro"
    )
    expect(
        page.get_by_role("heading", name="Installation")
    ).to_be_visible()


import pytest


@pytest.mark.parametrize(
    "path, expected_heading",
    [
        ("/docs/intro", "Installation"),
        ("/docs/writing-tests", "Writing tests"),
    ],
)
def test_documentation_pages(page: Page, path: str, expected_heading: str):
    page.goto(f"https://playwright.dev{path}")

    expect(
        page.get_by_role("heading", name=expected_heading).first
    ).to_be_visible()
