from tests.utils import *


def test_get_user_electives(client):
    """
    Simple getter
    """
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get('/get_user_electives', headers=headers)
    assert response.status_code == 200


def test_get_electives(client):
    """
    Simple getter
    """
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get('/get_electives', headers=headers)
    assert response.status_code == 200


def test_set_elective(client):
    """
    Use non-existing elective
    """
    token = register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "elective_name": "Psychology"
    }
    response = client.post('/set_elective', headers=headers, json=data)
    assert response.status_code == 404
