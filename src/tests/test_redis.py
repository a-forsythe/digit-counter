import redis


def test_redis_connection(client, redis_client):
    redis_client.set("test-key", "foobar")
    assert redis_client.get("test-key") == "foobar"
