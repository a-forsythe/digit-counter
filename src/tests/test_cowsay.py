def test_hello(client):
    r = client.get("/cowsay?s=hello")
    assert r.status_code == 200

    text = r.data.decode("utf-8")
    assert "hello" in text
    assert "^__^" in text
    assert "(oo)\\___" in text


def test_whitespace(client):
    r = client.get("/cowsay?s=hello%20world")
    assert "hello world" in r.data.decode("utf-8")
