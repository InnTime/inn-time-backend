from tests.utils import *


def test_login_fail_1(client):
    """
    Login with wrong credentials
    """
    response = login(client)
    assert response.status_code == 401


def test_login_fail_2(client):
    """
    Login with missing password field
    """
    response = login(client, password="")
    assert response.status_code == 401


def test_register_fail_1(client):
    """
    Register with missing password field
    """
    response = register(client, password="")
    assert response.status_code == 401


def test_register_success(client):
    """
    Successful registration
    """
    response = register(client)
    assert response.status_code == 200


def test_register_fail_2(client):
    """
    Register with already registered email
    """
    response = register(client)
    assert response.status_code == 200

    response = register(client)
    assert response.status_code == 400


def test_login_success(client):
    """
    Successful login
    """
    register_and_login(client)


def test_wrong_token(client):
    """
    Update user with wrong token
    """
    register_and_login(client)
    token = "eyJhbHciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4OTA5MjU4MywianRpIjoiYjExNjRlN2UtZDk2ZC00M2JmLWE0NDEtNWQ2OTJmYTU2YTk1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTIwLCJuYmYiOjE2ODkwOTI1ODMsImV4cCI6MTY5MDMwMjE4M30.YriDtBXUzRYpIVF41jwAXeRHt3mM3S8NhYTUsdsgJZU"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "password": "new_password"
    }
    response = client.put('/update_user', headers=headers, json=data)
    assert response.status_code == 422


def test_update_user(client):
    """
    Update user with correct token and check if password is updated
    """
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "password": "new_password"
    }
    response = client.put('/update_user', headers=headers, json=data)
    assert response.status_code == 200

    response = login(client)
    assert response.status_code == 401

    response = login(client, password="new_password")
    assert response.status_code == 200


def test_set_user_group_fail_1(client):
    """
    Such group does not exist
    """
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "group_id": 1
    }
    response = client.put('/set_user_group', headers=headers, json=data)
    assert response.status_code == 400


def test_set_user_group_fail_2(client):
    """
    Wrong group_id type
    """
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "group_id": "string"
    }
    response = client.put('/set_user_group', headers=headers, json=data)
    assert response.status_code == 400


def test_set_user_group_fail_3(client):
    """
    Empty payload
    """
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "group_id": ""
    }
    response = client.put('/set_user_group', headers=headers, json=data)
    assert response.status_code == 400


def test_logout(client):
    """
    Check if logout actually deletes token
    """
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post('/logout', headers=headers)
    assert response.status_code == 200

    data = {
        "password": "new_password"
    }
    response = client.put('/update_user', headers=headers, json=data)
    assert response.status_code == 422
