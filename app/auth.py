import base64
import hashlib
import hmac
import json
import os
import time

from .db import get_user

SECRET = os.getenv("APP_SECRET", "replace-me")
HEADER = {"alg": "HS256", "typ": "JWT"}


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def sign(data: bytes) -> str:
    return b64url(hmac.new(SECRET.encode(), data, hashlib.sha256).digest())


def create_jwt(payload: dict, exp_sec: int = 3600) -> str:
    header = b64url(json.dumps(HEADER, separators=(",", ":")).encode())
    new_payload = payload.copy()
    new_payload.update({"exp": int(time.time()) + exp_sec})
    body = b64url(json.dumps(new_payload, separators=(",", ":")).encode())
    signature = sign(f"{header}.{body}".encode())
    return f"{header}.{body}.{signature}"


def verify_user(username: str, password: str) -> bool:
    user = get_user(username)
    return bool(user and user["password"] == password)
