
from playwright.sync_api import Page, expect

from config.settings import PLAYWRIGHT_DOCS_URL


class PlaywrightDocsPage:
    def __init__(self, page: Page):
        self.page = page

    def open_homepage(self):
        self.page.goto(
            PLAYWRIGHT_DOCS_URL,
            wait_until="domcontentloaded",
        )

    def open_documentation_page(self, path: str):
        url = f"{PLAYWRIGHT_DOCS_URL.rstrip('/')}/{path.lstrip('/')}"
        self.page.goto(
            url,
            wait_until="domcontentloaded",
        )

    def click_get_started(self):
        self.page.get_by_role(
            "link", name="Get started"
        ).click()

    def verify_homepage_title(self):
        expect(self.page).to_have_title(
            "Fast and reliable end-to-end testing for modern web apps | Playwright"
        )

    def verify_get_started_link_visible(self):
        expect(
            self.page.get_by_role("link", name="Get started")
        ).to_be_visible()
