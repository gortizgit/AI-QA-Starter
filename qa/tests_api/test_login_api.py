import requests, yaml
from pathlib import Path

BASE_URL = "http://127.0.0.1:8000"

def test_login_contract_and_success():
    # contract smoke
    spec = yaml.safe_load(Path("contracts/auth_openapi.yaml").read_text())
    assert '/auth/login' in spec['paths']

    # happy path
    r = requests.post(f"{BASE_URL}/auth/login", json={"username":"demo","password":"P@ssw0rd"})
    assert r.status_code == 200
    j = r.json()
    assert 'access_token' in j and j['token_type'] == 'bearer'

def test_login_unauthorized():
    r = requests.post(f"{BASE_URL}/auth/login", json={"username":"demo","password":"bad"})
    assert r.status_code == 401
