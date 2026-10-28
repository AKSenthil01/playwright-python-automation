from playwright.sync_api import Page


class BasePage:
    """Shared browser-page behavior for application page objects."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        """Navigate to a URL after the document has been parsed."""
        self.page.goto(url, wait_until="domcontentloaded")
