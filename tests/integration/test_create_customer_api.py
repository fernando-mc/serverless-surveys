import requests
from tests.integration.utils import (
    get_http_api_endpoint_url,
    get_auth0_bearer_token,
    get_client_id
)
from tests.utils.dev_dynamodb_table import dev_table

BEARER_TOKEN = get_auth0_bearer_token()
CUSTOMER_ID = get_client_id() + '@clients'
BASE_URL = get_http_api_endpoint_url('test-surveys', 'dev')
AUTHORIZATION_HEADERS = {'Authorization': 'Bearer ' + BEARER_TOKEN}


def test_create_customer_returns_json():
    url = BASE_URL + '/customer'
    jsontest_item = {
        "profile_data": {"some": "jsondata"}
    }
    request = requests.post(
        url,
        json=jsontest_item,
        headers=AUTHORIZATION_HEADERS
    )
    jsontest_item['customer_id'] = CUSTOMER_ID
    assert request.json() == jsontest_item


def test_create_customer_saves_dynamodb_item():
    url = BASE_URL + '/customer'
    itemtest_item = {
        "profile_data": {"some": "saveditemtest"}
    }
    requests.post(url, json=itemtest_item, headers=AUTHORIZATION_HEADERS)
    expected_item = {
        'PK': 'CUSTOMER#' + CUSTOMER_ID,
        'SK': 'PROFILE#' + CUSTOMER_ID,
        'customer_id': CUSTOMER_ID,
        'profile_data': {'some': 'saveditemtest'}
    }
    table = dev_table()
    item = table.get_item(Key={
        'PK': 'CUSTOMER#' + CUSTOMER_ID,
        'SK': 'PROFILE#' + CUSTOMER_ID
    })['Item']
    assert expected_item == item


def test_create_customer_returns_saved_item():
    url = BASE_URL + '/customer'
    itemtest_item = {
        "profile_data": {"some": "saveditemtest"}
    }
    request = requests.post(
        url,
        json=itemtest_item,
        headers=AUTHORIZATION_HEADERS
    )
    itemtest_item['customer_id'] = CUSTOMER_ID
    assert request.json() == itemtest_item
