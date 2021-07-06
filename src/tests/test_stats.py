from __version__ import version


def test_stats(client):
    r = client.get("/stats")
    assert r.status_code == 200
    assert int(r.json["num"]) > 0
    assert r.json["version"] == version
