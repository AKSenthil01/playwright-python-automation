# Playwright Python Automation Framework

A Python-based UI test automation framework built with Playwright and pytest. The project demonstrates the Page Object Model (POM), data-driven testing, positive and negative test scenarios, fixture isolation, browser automation, and continuous integration with GitHub Actions.

## Project Overview

This framework automates selected user workflows on [Automation Exercise](https://automationexercise.com) and validates navigation and documentation pages on [Playwright](https://playwright.dev).

The project is intended to demonstrate maintainable UI automation practices, reusable page objects, test-data separation, meaningful assertions, and cross-browser execution.

## Key Features

- **Playwright with Python:** Browser automation using Playwright's synchronous API.
- **pytest:** Test execution, fixtures, parameterization, and markers.
- **Page Object Model (POM):** Separates page interactions from test logic.
- **Data-driven testing:** Loads positive product-search test data from JSON.
- **Positive and negative testing:** Validates successful product searches and searches with no matching products.
- **Cart workflow validation:** Checks the add-to-cart interaction and its HTTP response status.
- **Fixture lifecycle testing:** Verifies that tests receive independent page state.
- **Reusable documentation page object:** Centralizes navigation and checks for Playwright documentation pages.
- **Cross-browser testing:** Supports Chromium, Firefox, and WebKit.
- **Failure diagnostics:** Configures screenshots and tracing to be retained on test failures.
- **HTML reporting:** Uses pytest-html to generate test reports.
- **Configurable base URL:** Supports overriding the Automation Exercise base URL through the `BASE_URL` environment variable.
- **Continuous integration:** Runs browser-specific test jobs using GitHub Actions.

## Technology Stack

- Python 3.11
- Playwright for Python
- pytest
- pytest-playwright
- pytest-html
- JSON test data
- Git and GitHub
- GitHub Actions

## Project Structure

```text
playwright-python-automation/
├── .github/
│   └── workflows/
│       └── tests.yml
├── config/
│   └── settings.py
├── data/
│   └── product_search_data.json
├── pages/
│   ├── home_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── playwright_docs_page.py
├── tests/
│   ├── conftest.py
│   ├── test_home_page.py
│   ├── test_products_page.py
│   ├── test_product_search.py
│   ├── test_product_search_negative.py
│   ├── test_add_to_cart.py
│   ├── test_fixture_lifecycle.py
│   └── test_web_workflows.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.11 or a compatible supported Python version
- pip
- Git
- Internet access for the external websites used by the tests

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/AKSenthil01/playwright-python-automation.git
cd playwright-python-automation
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
python -m playwright install
```

## Running the Tests

### Run the complete suite

```powershell
python -m pytest -v
```

### Run tests using Chromium

```powershell
python -m pytest --browser chromium
```

### Run tests using Firefox

```powershell
python -m pytest --browser firefox
```

### Run tests using WebKit

```powershell
python -m pytest --browser webkit
```

### Run only smoke tests

```powershell
python -m pytest -m smoke
```

### Run regression tests

```powershell
python -m pytest -m regression
```

### Run product-search tests

```powershell
python -m pytest tests/test_product_search.py tests/test_product_search_negative.py -v
```

### Generate an HTML report

Create the report directory and run pytest:

```powershell
New-Item -ItemType Directory -Force reports
python -m pytest --browser chromium --html=reports\report.html --self-contained-html
```

After execution, open `reports\report.html` in a browser.

The command-line report option creates an HTML report for that test run. The GitHub Actions workflow also generates browser-specific reports and uploads them as workflow artifacts when available.

## Screenshots and Tracing

The project configures the following pytest-playwright options in `pytest.ini`:

```ini
addopts = -v --screenshot only-on-failure --tracing retain-on-failure
```

These options request screenshots and traces for failed tests. The available evidence depends on how the test run ends and which artifacts the runner retains.

When debugging a failure, inspect the pytest output and any available screenshots or traces before changing the test or its assertions.

## Test Coverage

The current suite covers:

- Loading the Automation Exercise homepage.
- Opening the products page.
- Searching for products using JSON-driven test data.
- Checking behavior for nonexistent products.
- Adding a product to the cart and checking the associated HTTP response.
- Verifying independent page state between tests.
- Checking the Playwright documentation homepage title.
- Verifying the visibility of the Get started link.
- Checking navigation to the installation documentation.
- Validating headings on selected documentation pages.

The suite validates these selected workflows; it is not intended to represent exhaustive coverage of either website.

## GitHub Actions CI

The workflow is defined in `.github/workflows/tests.yml`.

It is configured to run on:

- Pushes to the repository
- Pull requests
- Manual workflow dispatch

The workflow uses a browser matrix with separate jobs for:

- Chromium
- Firefox
- WebKit

Each job installs Python dependencies and its required Playwright browser, runs the test suite, generates an HTML report, and attempts to upload the report as a workflow artifact.

### Verified CI Status

**Commit:** `3b5ef7e` — `Add pytest smoke and regression markers`

The current revision was pushed to the `master` branch. The local test run passed, and all three browser jobs in GitHub Actions were reported as passing.

These results apply to the verified revision and test scope; they do not imply that every browser, operating system, or possible application scenario has been tested.

## Current Revision Status

- **Branch:** `master`
- **Commit:** `3b5ef7e`
- **Local environment:** Windows, Python 3.11.9, pytest 9.1.1
- **Latest recorded local test result:** 15 passed in 78.79 seconds using Chromium.
- **GitHub Actions:** Chromium, Firefox, and WebKit jobs passed, as verified after the push.
- **Version control:** Changes pushed to GitHub; the local branch was confirmed synchronized with `origin/master`.

## Planned Improvements

Potential future enhancements include:

- Expanding test-data coverage and scenario variety.
- Improving failure diagnostics and making failure evidence easier to inspect.
- Improving resilience to external website changes.
- Adding further negative, boundary, and workflow scenarios where appropriate.
- Reviewing report artifacts and diagnostic evidence during future CI runs.

These are future improvements, not claims that the features are already implemented.

## Repository

GitHub: https://github.com/AKSenthil01/playwright-python-automation

## Disclaimer

This is a learning and portfolio project that automates selected workflows on publicly accessible websites. External website availability, content, and behavior can change and may affect test results.
