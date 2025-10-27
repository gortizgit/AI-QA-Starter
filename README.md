# 🚀 AI-QA-Starter

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-E2E%20Tests-brightgreen)
![Selenium](https://img.shields.io/badge/Selenium-Web%20Automation-orange)
![Applitools](https://img.shields.io/badge/Visual%20AI-Applitools-blueviolet)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![CI](https://github.com/<your-user>/AI-QA-Starter/actions/workflows/ci.yml/badge.svg)

---

**AI-QA-Starter** is a modern, ready-to-use **QA automation starter kit** that combines a **web backend**, **UI testing**, **AI-based test generation**, and a complete **CI/CD pipeline**.  
It’s designed to help QA engineers and developers build intelligent test automation environments quickly.

---

## 🧩 What’s Included
- 🧠 **FastAPI** — backend with demo login (JWT authentication)
- 🧪 **Pytest + Playwright** — E2E, API, and Unit testing
- 🌐 **Selenium** — classic web automation
- 👁️ **Applitools Visual AI** — intelligent visual validation
- 🤖 **AI Modules** — automatic test generation and risk-based prioritization
- 📜 **OpenAPI Contract** — `/auth/login` endpoint
- ⚙️ **GitHub Actions** — CI pipeline for linting, testing, and reporting

---

## 🧭 Quickstart

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-user>/AI-QA-Starter.git
cd AI-QA-Starter
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install --with-deps
```

### 4️⃣ Run the backend
```bash
uvicorn app.main:app --reload
```
Then open your browser at:  
👉 **http://127.0.0.1:8000**

Default credentials:  
`username=demo` | `password=P@ssw0rd`

---

## 🧪 Running Tests

### ✅ Run all tests (Unit + API + E2E)
```bash
pytest -q
```

### 🧭 Playwright (E2E / UI)
```bash
pytest -q qa/tests_e2e
# To run with browser UI visible:
pytest -q qa/tests_e2e --headed
```

### ⚙️ API Tests
```bash
pytest -q qa/tests_api
```

### 🧩 Unit Tests
```bash
pytest -q qa/tests_unit
```

### 🌐 Selenium (Web)
```bash
pytest -q selenium/tests
```

---

## 👁️ Visual AI with Applitools

1️⃣ Get your API key from [Applitools](https://eyes.applitools.com) → **Profile → My API Key**  
2️⃣ Set it as an environment variable:

```bash
# macOS / Linux
export APPLITOOLS_API_KEY=xxxxx

# Windows PowerShell
$Env:APPLITOOLS_API_KEY="xxxxx"

# (Optional - persistent key on Windows)
setx APPLITOOLS_API_KEY "xxxxx"
```

3️⃣ Run the visual regression test:
```bash
pytest -q selenium/tests/test_login_visual_ai.py
```

4️⃣ View results at:  
👉 [https://eyes.applitools.com](https://eyes.applitools.com)

---

## 📁 Project Structure
```
app/                 # FastAPI backend + UI templates
qa/                  # Playwright E2E, API, and Unit tests
selenium/            # Selenium Page Objects + Visual AI test
ai/                  # AI modules: test generation & risk prioritization
contracts/           # OpenAPI definition for /auth/login
.github/workflows/   # GitHub Actions CI pipeline
docs/                # Documentation and setup guides
```

---

## 🔐 Security (Demo)
This project is for demonstration purposes.  
For production, you should:
- Store secrets in `.env` files or vaults  
- Hash user passwords properly  
- Add rate-limiting and secure headers  
- Enforce HTTPS and CSRF protection  

---

## 🐙 Push to GitHub
```bash
git init
git add .
git commit -m "feat: initial AI-QA-Starter"
git branch -M main
git remote add origin https://github.com/<your-user>/AI-QA-Starter.git
git push -u origin main
```

---

## 💡 Tips
- Run `pytest -v` for verbose output  
- Add `--headed` to Playwright for visible runs  
- Update your Playwright browsers regularly:  
  ```bash
  python -m playwright install --with-deps
  ```
- Troubleshooting Visual AI:  
  - Ensure your `APPLITOOLS_API_KEY` is valid  
  - Check network/firewall if `401 Unauthorized` occurs  

---

📘 **Full Setup Guide:** See [docs/AI-QA-Starter-Setup-&-Run-Guide.md](docs/AI-QA-Starter-Setup-&-Run-Guide.md)

**Developed for modern QA engineers** 🧠  
Combining **AI + Automation + CI/CD** in one starter project.
