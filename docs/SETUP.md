# AI-QA-Starter — Setup & Run Guide

## 1️⃣ Overview — What This Project Does
**AI-QA-Starter** is a **complete AI-driven QA Automation Starter Kit**, built to help you create, test, and deploy automated quality pipelines using modern technologies and artificial intelligence.

It includes:
- **Backend & UI:** FastAPI app with a login form (`/`) and authentication endpoint (`/auth/login`).
- **Automated Testing:**  
  - E2E/UI with **Playwright (Pytest)**  
  - **API** and **Unit** tests with Pytest  
  - **Selenium** (classic web automation)  
  - **Applitools Visual AI** for intelligent visual regression testing  
- **AI Modules:**  
  - `generate_tests.py` — Generates test cases from user stories using LLMs.  
  - `risk_selector.py` — Prioritizes tests based on recent code changes.  
- **Contracts:** `/auth/login` endpoint documented via OpenAPI.  
- **CI/CD Pipeline:** Full GitHub Actions workflow with linting, testing, and Visual AI validation.

---

## 2️⃣ Requirements
- Python **3.11+**
- **Google Chrome** (for Selenium)
- **Git**
- (Optional) **Applitools API Key** for Visual AI
- (Optional) **Make** or PowerShell for scripting convenience

---

## 3️⃣ Installation
```bash
# 1. Clone the repository
git clone https://github.com/<your-user>/AI-QA-Starter.git
cd AI-QA-Starter

# 2. Create a virtual environment
python -m venv .venv
# Activate:
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Install Playwright browsers
python -m playwright install --with-deps
```

---

## 4️⃣ Run the Backend
```bash
uvicorn app.main:app --reload
# Open http://127.0.0.1:8000
# Default credentials: username=demo | password=P@ssw0rd
```

---

## 5️⃣ Run Tests

### A) All Tests (Unit + API + E2E)
```bash
pytest -q
```

### B) Playwright (E2E/UI)
```bash
pytest -q qa/tests_e2e
# To view browser UI:
pytest -q qa/tests_e2e --headed
```

### C) API Tests
```bash
pytest -q qa/tests_api
```

### D) Unit Tests
```bash
pytest -q qa/tests_unit
```

### E) Selenium (Web)
```bash
pytest -q selenium/tests
```

### F) Visual AI (Applitools)
1. Set your API key:
   ```bash
   export APPLITOOLS_API_KEY=xxxxx   # macOS/Linux
   $Env:APPLITOOLS_API_KEY="xxxxx"   # Windows PowerShell
   ```
2. Run the visual test:
   ```bash
   pytest -q selenium/tests/test_login_visual_ai.py
   ```

---

## 6️⃣ Environment Variables
| Variable | Description | Default |
|-----------|--------------|----------|
| `APP_SECRET` | JWT secret key | `replace-me` |
| `BASE_URL` | Target app base URL | `http://127.0.0.1:8000` |
| `APPLITOOLS_API_KEY` | Required for Visual AI tests | *None* |

---

## 7️⃣ CI/CD — GitHub Actions
Each push triggers:
1. Checkout & Python setup  
2. Dependency installation + Playwright setup  
3. Lint check with Ruff  
4. Run Unit + API + E2E tests  
5. Run Selenium tests (headless)  
6. Run Visual AI tests (if key provided)  
7. Report results & exit

---

## 8️⃣ AI Features
- **`generate_tests.py`:** uses LLMs (like GPT or HuggingFace) to generate test cases automatically.  
- **`risk_selector.py`:** uses Git diff analysis to prioritize risky test areas.

---

## 9️⃣ Troubleshooting
| Issue | Possible Fix |
|-------|----------------|
| `chromedriver not found` | Update Chrome or reinstall Selenium |
| `pytest-playwright` errors | Run `python -m playwright install --with-deps` |
| `401 Unauthorized` | Use default credentials: demo / P@ssw0rd |
| Visual AI not running | Add `APPLITOOLS_API_KEY` environment variable |

---

## 10️⃣ Architecture Diagram
Add this image in your README:

![AI-QA-Starter Architecture](docs/AI-QA-Starter-Architecture.png)

---

📘 **Architecture Diagram (PNG included)**  
Use the provided image file `AI-QA-Starter-Architecture.png` in your documentation.

---

## 11️⃣ Configure Visual AI (Applitools)

This step is optional. If you don’t set the key, the Visual AI step in CI will be skipped safely.

**Create the repository secret:**
1. Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**  
2. Set:
   - **Name:** `APPLITOOLS_API_KEY`
   - **Secret:** your real Applitools API key (from https://eyes.applitools.com → avatar → **My API Key**)
3. Click **Add secret**.

**How the CI uses it**
- The workflow maps the secret to an environment variable and runs Visual AI only if it’s present:
  ```yaml
  env:
    APPLITOOLS_API_KEY: ${{ secrets.APPLITOOLS_API_KEY }}

  - name: Visual AI (Applitools)
    if: ${{ env.APPLITOOLS_API_KEY != '' }}
    run: pytest -q selenium/tests/test_login_visual_ai.py

