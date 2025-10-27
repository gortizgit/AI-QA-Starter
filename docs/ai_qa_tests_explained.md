# AI-QA-Starter — Detailed Test Documentation

## Overview
This document explains **every automated test** included in the `AI-QA-Starter` repository. It describes what each test validates, how it works, which system components it covers, and common failure points. These tests collectively validate the integration between the FastAPI backend, Playwright (UI/E2E), Selenium (browser automation), API layer, and AI-powered validation (Applitools Visual AI).

---

## QA (Playwright + API + Unit)

### 1. `qa/tests_e2e/test_login_e2e.py`
**Scope:** End-to-End UI flow (HTML + backend FastAPI)

#### `test_login_success`
- **Purpose:** Validates that a user can log in successfully using the correct credentials (`demo / P@ssw0rd`).
- **How:**
  - Opens the FastAPI app UI (`/` route).
  - Fills the username and password fields.
  - Clicks the **Sign in** button.
  - Waits for the `<pre id="result">` element to appear.
- **Expected Result:** The element contains a valid JWT `access_token`.
- **Common Issues:**
  - Missing selectors or page load delays.
  - Backend not running or database not initialized.

#### `test_login_invalid`
- **Purpose:** Ensures that incorrect credentials are rejected properly.
- **How:**
  - Submits `demo / bad` as credentials.
  - Waits for the result element and checks its content.
- **Expected Result:**
  - The response contains `{ "detail": "Invalid credentials" }` or status text `401`.
- **Common Issues:**
  - Assertion too strict (text mismatch between JSON and numeric code).

**Command to run this suite:**
```bash
pytest -q qa/tests_e2e/test_login_e2e.py
```

---

### 2. `qa/tests_api/test_login_api.py`
**Scope:** API contract validation for `/auth/login`

#### `test_login_api_success`
- **Purpose:** Validates successful authentication at the API level.
- **How:** Sends a POST request to `/auth/login` with JSON `{ "username": "demo", "password": "P@ssw0rd" }`.
- **Expected Result:**
  - Response `status_code == 200`.
  - JSON includes a valid `access_token`.

#### `test_login_api_invalid`
- **Purpose:** Validates rejection of invalid credentials.
- **How:** Sends `{ "username": "demo", "password": "bad" }`.
- **Expected Result:**
  - Response `status_code == 401`.
  - JSON includes `detail == "Invalid credentials"`.

**Command to run this suite:**
```bash
pytest -q qa/tests_api
```

---

### 3. `qa/tests_unit/*`
**Scope:** Core functionality validation (unit level)

#### `test_db_returns_demo_user`
- **Purpose:** Ensures the default demo user exists in the SQLite database.
- **How:** Calls `get_user('demo')` and checks the return type and data.
- **Expected Result:**
  - Returns a dict containing `{ 'username': 'demo', 'password': 'P@ssw0rd' }`.

#### `test_create_jwt_contains_exp_and_three_segments`
- **Purpose:** Validates JWT token structure.
- **How:** Calls `create_jwt({ 'sub': 'demo' })`.
- **Expected Result:**
  - Returns a valid JWT string with 3 segments (header.payload.signature).
  - Contains an `exp` field inside the payload.

**Command to run this suite:**
```bash
pytest -q qa/tests_unit
```

---

## Selenium (Browser Automation)

### 4. `selenium/tests/test_login_selenium.py`
**Scope:** Full browser test using Chrome + Selenium WebDriver.

#### `test_login_success_selenium`
- **Purpose:** Confirms successful login from the user interface using Selenium.
- **How:**
  - Opens the login page.
  - Enters valid credentials.
  - Clicks **Sign in**.
  - Waits for the result element.
- **Expected Result:** The `<pre id="result">` element contains an `access_token`.

#### `test_login_invalid_selenium`
- **Purpose:** Ensures the page shows an error message when the credentials are wrong.
- **How:** Enters `demo / bad`, submits, and waits for `#result`.
- **Expected Result:** Displays either `Invalid credentials` or `401`.

**Command to run this suite:**
```bash
pytest -q selenium/tests/test_login_selenium.py
```

---

### 5. `selenium/tests/test_login_visual_ai.py`
**Scope:** Visual Regression using Applitools Eyes.

#### `test_visual_login_page`
- **Purpose:** Detects unintended UI changes in the login page layout and style.
- **How:**
  - Opens the page with Selenium.
  - Initializes Applitools Eyes with the provided API key.
  - Takes a full-page snapshot (`eyes.check_window()`).
  - Compares it to the baseline snapshot stored in Applitools.
- **Expected Result:** No visual diffs unless intentional UI modifications were made.
- **Common Issues:**
  - Missing or invalid `APPLITOOLS_API_KEY`.
  - Layout differences due to resolution or styling changes.

**Command to run this suite:**
```bash
pytest -q selenium/tests/test_login_visual_ai.py
```

---

## Test Layer Coverage Summary
| Layer | Test Files | What It Ensures |
|-------|-------------|-----------------|
| **Unit** | `qa/tests_unit/*` | Database setup and JWT helper functions work as expected. |
| **API** | `qa/tests_api/test_login_api.py` | The `/auth/login` endpoint adheres to its contract (200/401, valid token). |
| **E2E (Playwright)** | `qa/tests_e2e/test_login_e2e.py` | UI and backend communicate correctly through the login flow. |
| **Selenium** | `selenium/tests/test_login_selenium.py` | Browser automation works and mirrors Playwright's E2E coverage. |
| **Visual AI** | `selenium/tests/test_login_visual_ai.py` | Detects visual regressions and layout changes via Applitools. |

---

## How to Execute All Tests
To run the entire suite locally (Windows or Linux):
```bash
pytest -q
```

Or to run each test layer separately:
```bash
pytest -q qa/tests_unit
pytest -q qa/tests_api
pytest -q qa/tests_e2e
pytest -q selenium/tests/test_login_selenium.py
pytest -q selenium/tests/test_login_visual_ai.py
```

---

## Suggested Future Improvements
- Add **negative API cases** (empty fields, malformed JSON, rate-limit).
- Decode and validate JWT payload (`exp`, `sub`, `iat`) in unit tests.
- Parametrize tests with multiple credential sets.
- Include **Playwright screenshot attachments** on failures.
- Add a **matrix strategy** to the CI pipeline (browsers: `chromium`, `firefox`, `webkit`).

---

**Author:** QA Automation Team  
**Project:** AI-QA-Starter  
**Last Updated:** 2025-10-27