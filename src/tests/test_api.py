def test_missing_param(client):
    r = client.get("/")
    assert r.status_code == 400
    assert r.json["error"] == "Missing URL parameter 's'"


def test_no_digits(client):
    r = client.get("/?s=hello")
    assert r.status_code == 200
    assert r.json["count"] == 0
    assert "no digits" in r.json["message"]


def test_one_digit(client):
    r = client.get("/?s=hello5")
    assert r.status_code == 200
    assert r.json["count"] == 1
    assert " 1 digit" in r.json["message"]


def test_ten_digits(client):
    r = client.get("/?s=hello5566778899")
    assert r.status_code == 200
    assert r.json["count"] == 10
    assert " 10 digits" in r.json["message"]


def test_many_digits(client):
    s = ("1234567890" * 300) + "_1231"
    r = client.get(f"/?s={s}")
    assert r.status_code == 200
    assert r.json["count"] == 3004
    assert any(x in r.json["message"] for x in ("Tarnation!", "Consarnit!"))
