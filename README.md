# Playwright Python UI Automation Framework

A Python-based browser UI automation portfolio project built with Playwright and pytest. It demonstrates maintainable test automation using the Page Object Model (POM), positive and negative product search, cart workflows, cross-browser execution, and HTML reporting.

## Features

- Browser UI automation using Playwright and pytest
- Page Object Model with reusable page classes
- Homepage title and page navigation validation
- Positive and negative product-search scenarios
- Add-to-cart and cart-content validation
- Pytest fixtures and configuration
- Accessible locators and explicit assertions
- Screenshot capture on test failure
- Cross-browser testing with Chromium, Firefox, and WebKit
- Standalone HTML test reports using pytest-html
- Configurable base URL using an environment variable

## Technology Stack

- Python 3.11
- Playwright for Python
- pytest
- pytest-playwright
- pytest-html
- Chromium, Firefox, and WebKit

## Project Structure

```text
playwright-python-automation/
├── config/
│   └── settings.py
├── pages/
│   ├── __init__.py
│   ├── home_page.py
│   ├── products_page.py
│   └── cart_page.py
├── tests/
│   ├── conftest.py
│   ├── test_home_page.py
│   ├── test_products_page.py
│   ├── test_product_search.py
│   ├── test_product_search_negative.py
│   ├── test_web_workflows.py
│   └── test_add_to_cart.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.11 or a compatible Python version
- pip
- Internet access to install dependencies and access the test websites

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

Run against a specific browser:

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
python -m pytest --browser chromium --browser firefox --browser webkit --html=reports\report.html --self-contained-html
```

Open `reports\report.html` in a browser to review the results.

## Test Coverage

The suite covers homepage validation, product-page validation, positive and negative product search, add-to-cart and cart-content verification, and navigation workflows on the Playwright documentation website.

## Verified Results

- 30 browser-specific test executions passed across Chromium, Firefox, and WebKit.
- A subsequent three-browser run also passed all 30 executions and generated a standalone HTML report.
- Latest recorded three-browser run: 30 passed, 0 failed in 156.88 seconds.

These results describe the local test run; they do not imply that CI/CD has been configured or that the tests have been executed on every operating system.

## Configuration

The base URL is configured in `config/settings.py`. It can be overridden through the `BASE_URL` environment variable when running tests against a suitable target environment.

The tests use public websites, so network availability, site changes, and third-party behavior may affect results.

## Planned Improvements

- GitHub Actions CI/CD integration
- Automated test execution on pushes and pull requests
- Uploading HTML reports as CI artifacts
- Further test-data and failure-diagnostics improvements
