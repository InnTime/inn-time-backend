def register(client, email="real@email.com", password="123"):
    data = {
        "email": email,
        "password": password
    }
    response = client.post('/register', json=data)

    return response


def login(client, email="real@email.com", password="123"):
    data = {
        "email": email,
        "password": password
    }
    response = client.post('/login', json=data)

    return response


def register_and_login(client):
    """
    @return: accessToken
    """
    response = register(client)
    assert response.status_code == 200

    response = login(client)
    assert response.status_code == 200

    return response.json['accessToken']
