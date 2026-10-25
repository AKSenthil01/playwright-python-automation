# Playwright Python UI Automation Framework

A Python-based browser UI automation portfolio project built with Playwright and pytest. The framework demonstrates maintainable test automation using the Page Object Model (POM), data-driven positive and negative product search, cart workflows, fixture lifecycle checks, cross-browser configuration, and HTML reporting.

## Features

- Browser UI automation using Playwright for Python and pytest
- Page Object Model with reusable page classes
- Homepage and product-page validation
- Data-driven positive product-search scenarios using JSON test data
- Negative product-search scenarios
- Add-to-cart and cart-content verification
- Pytest fixtures and configuration
- Accessible locators and explicit assertions
- Screenshot capture and tracing configured for failure diagnostics
- Chromium, Firefox, and WebKit execution support
- Standalone HTML reports using pytest-html
- Configurable base URL using the `BASE_URL` environment variable
- GitHub Actions workflow configured for push, pull-request, and manual triggers
- Separate CI jobs for Chromium, Firefox, and WebKit, with HTML report artifacts

## Technology Stack

- Python 3.11
- Playwright for Python
- pytest
- pytest-playwright
- pytest-html
- Chromium, Firefox, and WebKit
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
│   ├── __init__.py
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
│   ├── test_web_workflows.py
│   ├── test_add_to_cart.py
│   └── test_fixture_lifecycle.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.11 or a compatible Python version
- pip
- Internet access to install dependencies and access the public test websites

## Setup on Windows

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

Install all three Playwright browser engines:

```powershell
python -m playwright install chromium firefox webkit
```

## Running Tests

Run the complete suite using the default browser configuration:

```powershell
python -m pytest
```

Run against an individual browser:

```powershell
python -m pytest --browser chromium
python -m pytest --browser firefox
python -m pytest --browser webkit
```

Run against all three browsers:

```powershell
python -m pytest --browser chromium --browser firefox --browser webkit
```

Generate a standalone HTML report:

```powershell
New-Item -ItemType Directory -Force reports
python -m pytest --browser chromium --html=reports\report.html --self-contained-html
```

Open `reports\report.html` in a browser to review the results.

## Test Coverage

The current suite includes:

- Homepage title validation
- Product-page validation
- Data-driven positive product search
- Negative search for nonexistent products
- Add-to-cart response and confirmation checks
- Cart-content verification
- Playwright documentation homepage and navigation checks
- Documentation-page heading checks
- Fixture lifecycle and page isolation checks

## GitHub Actions CI

The workflow at `.github/workflows/tests.yml` is configured to run on pushes, pull requests, and manual dispatches.

It uses a browser matrix with separate jobs for Chromium, Firefox, and WebKit. Each job installs Python dependencies and its browser, executes the pytest suite, generates a self-contained HTML report, and uploads the report as a workflow artifact.

**Current revision status:** The latest local test run passed all 14 tests in 73.53 seconds using Chromium on Windows with Python 3.11.9 and pytest 9.1.1. The current working changes have not yet been pushed, so GitHub Actions results for this revision remain unverified.
**Historical result:** An earlier project revision passed all three browser jobs in GitHub Actions. That result does not establish that the current unpushed changes pass in CI.

## Configuration and Reliability Notes

The base URL is configured in `config/settings.py` and can be overridden through the `BASE_URL` environment variable when running against a suitable target environment.

The tests use public websites. Network availability, website changes, bot protection, and third-party behavior may affect test outcomes.

## Planned Improvements

- Push and validate the current revision through GitHub Actions
- Review cross-browser results for the current revision
- Continue improving test-data coverage and failure diagnostics
- Review test stability against external website changes
