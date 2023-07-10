def test_login_fail(client):
    data = {
        "email": "not@exist.com",
        "password": "123"
    }
    response = client.post('/login', json=data)
    assert response.status_code == 401


def test_register_fail_1(client):
    data = {
        "email": "real@email.com"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 400


def test_register_success(client):
    data = {
        "email": "real@email.com",
        "password": "123"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 200

    data = {
        "email": "real@email.com",
        "password": "123"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 400


def test_login_success(client):
    data = {
        "email": "real@email.com",
        "password": "123"
    }
    response = client.post('/login', json=data)
    assert response.status_code == 200


def test_update_password(client):
    # get token
    data = {
        "email": "real@email.com",
        "password": "123"
    }
    response = client.post('/login', json=data)
    assert response.status_code == 200

    # update password
    headers = {"Authorization": f"Bearer {response.json['accessToken']}"}
    data = {
        'password': 'new_password'
    }
    assert response.status_code == 200

    # check if password correct
    data = {
        "email": "real@email.com",
        "password": "new_password"
    }
    response = client.post('/login', json=data)
    assert response.status_code == 200
