
import json
from unittest.mock import patch

import pytest
from accounts.messages import *
from django.urls import reverse

from .extra import DUMMY_TOKEN, non_field_error

url = reverse('Admin_Change_Password')
pytestmark = pytest.mark.django_db

DATA = {
    "old_password": "1234",
    "password": "12345",
    "password2": "12345",
}


def test_admin_change_wrong_old_password(client, create_test_admin):
    token = create_test_admin

    DATA["old_password"] = "123"

    response = client.post(
        url, DATA, **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
    response_content = json.loads(response.content)

    assert response.status_code == WRONG_OLD_PASSWORD_STATUS
    assert response_content == non_field_error(WRONG_OLD_PASSWORD)


def test_wrong_confirm_password(client, create_test_admin):
    token = create_test_admin

    DATA["password2"] = "123456"

    response = client.post(
        url, DATA, **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
    response_content = json.loads(response.content)

    assert response.status_code == PASSWORD_AND_CONFIRM_PASSWORD_NOT_MATCH_STATUS
    assert response_content == non_field_error(
        PASSWORD_AND_CONFIRM_PASSWORD_NOT_MATCH)


@pytest.mark.xfail
@patch('accounts.views.get_tokens_for_user')
def test_change_password_success(patch_token, client, create_test_admin, admin_login):

    # == == == == == == == == Test Change Password == == == == == == == ==
    token = create_test_admin

    message = {
        "msg": PASSWORD_CHANGE_SUCCESS_MESSAGE
    }
    response = client.post(
        url, DATA, **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
    response_content = json.loads(response.content)

    assert response_content == message
    assert response.status_code == 200

# == == == == == == == == Test Login With Changed Password == == == == == == == ==

    response = admin_login(patch_token=patch_token,
                           client=client, email="admin@test.com", password="12345")
    response.status_code == 200
    response_content = json.loads(response.content)
    assert response_content == {
        "msg": LOGIN_SUCCESS_MESSAGE,
        "token": DUMMY_TOKEN
    }
