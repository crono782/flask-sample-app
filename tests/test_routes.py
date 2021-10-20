"""Module for basic route tests"""


def test_not_found(client):
    """Function to test index route

    Args:
        client (class): FlaskClient to use for testing
    """
    print(type(client))
    res = client.get("/asdf")
    assert res.status_code == 404
