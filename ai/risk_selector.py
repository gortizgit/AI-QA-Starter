import subprocess

def git_changed_files() -> list[str]:
    try:
        out = subprocess.check_output(["git","diff","--name-only","origin/main...HEAD"]).decode().splitlines()
        return out
    except Exception:
        return []

RULES = {
  "qa/tests_e2e/test_login_e2e.py": 5,
  "qa/tests_api/test_login_api.py": 4,
  "qa/tests_unit/test_auth_unit.py": 3,
  "selenium/tests/test_login_selenium.py": 4
}

def score(test_path: str, changed: set[str]) -> int:
    base = RULES.get(test_path, 1)
    touched = any(p in test_path or test_path.split('/')[-1].replace('_test','') in p for p in changed)
    return base + (3 if touched else 0)

if __name__ == "__main__":
    tests = ["qa/tests_e2e/test_login_e2e.py","qa/tests_api/test_login_api.py","qa/tests_unit/test_auth_unit.py","selenium/tests/test_login_selenium.py"]
    ch = set(git_changed_files())
    ranked = sorted(tests, key=lambda t: -score(t, ch))
    print("\n".join(ranked))
