# AI-QA-Starter

Starter listo para **web backend + UI + QA moderno** con:
- **FastAPI** (login demo con JWT simple)
- **Pytest + Playwright** (E2E/API/Unit)
- **Selenium (variant web)**
- **Applitools Visual AI** (validación visual)
- **AI modules** (generación de casos y priorización por riesgo)
- **OpenAPI contract** y **GitHub Actions** (CI)

## 🚀 Quickstart

```bash
# 1) Clonar y entrar
git clone <your-repo-url> AI-QA-Starter
cd AI-QA-Starter

# 2) Crear venv e instalar deps
python -m venv .venv
# Windows: .venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install --with-deps

# 3) Arrancar la app (dev)
uvicorn app.main:app --reload

# 4) Navega a
# http://127.0.0.1:8000

# 5) Ejecutar pruebas (unit, api, e2e)
pytest -q
```

## 🧪 Variantes de UI

### Playwright (default E2E)
```bash
pytest -q qa/tests_e2e
```

### Selenium (desktop web)
```bash
pytest -q selenium/tests
```

### Visual AI (Applitools + Selenium)
1) Consigue tu API Key y expórtala:
```bash
export APPLITOOLS_API_KEY=xxxxx
# PowerShell: $Env:APPLITOOLS_API_KEY="xxxxx"
```
2) Ejecuta el test visual:
```bash
pytest -q selenium/tests/test_login_visual_ai.py
```

## 📦 Estructura
```
app/                 # FastAPI + UI
qa/                  # Playwright + API + unit
selenium/            # Selenium POM + visual test (Applitools)
ai/                  # IA: generación de casos + priorización
contracts/           # OpenAPI /auth/login
.github/workflows/   # CI pipeline
```

## 🔐 Seguridad (demo)
Para prod agrega hash de passwords, .env para secret, rate-limit y mejores cabeceras.

## 🐙 Subir a GitHub
```bash
git init
git add .
git commit -m "feat: initial AI-QA-Starter"
git branch -M main
git remote add origin https://github.com/<your-user>/AI-QA-Starter.git
git push -u origin main
```
