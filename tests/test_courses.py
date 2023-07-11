from tests.utils import *


def test_get_user_courses(client):
    """
    Simple getter
    """
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get('/get_user_courses', headers=headers)
    assert response.status_code == 200


def test_get_courses(client):
    """
    Simple getter
    """
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get('/get_courses', headers=headers)
    assert response.status_code == 200


def test_get_all_groups(client):
    """
    Simple getter
    """
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get('/get_groups', headers=headers)
    assert response.status_code == 200
