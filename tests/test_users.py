def test_login_fail(client):
    data = {
        "email": "not@exist.com",
        "password": "123"
    }
    response = client.post('/login', json=data)

    assert response.status_code == 401
