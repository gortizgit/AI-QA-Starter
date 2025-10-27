from app.auth import verify_user

def test_verify_user_true():
    assert verify_user("demo","P@ssw0rd") is True

def test_verify_user_false():
    assert verify_user("demo","wrong") is False
