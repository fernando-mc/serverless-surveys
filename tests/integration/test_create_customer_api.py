import json
import requests
from tests.integration.utils import get_endpoint_url
from tests.utils.dev_dynamodb_table import dev_table


def gen_sample_customer_item(customer_id):
    return {
        "customer_id": customer_id,
        "profile_data": {"some": "data"}
    }


BASE_URL = get_endpoint_url('test-surveys', 'dev')


def test_create_customer_returns_json():
    url = BASE_URL + '/customer'
    jsontest_item = gen_sample_customer_item('jsontest')
    request = requests.post(url, json=jsontest_item)
    assert request.text == json.dumps(jsontest_item)


# def test_create_customer_saves_dynamodb_item():
#     url = BASE_URL + '/customer'
#     itemtest_item = gen_sample_customer_item('itemtest')
#     request = requests.post(url, json=itemtest_item)
#     table = dev_table()
#     item = table.get_item(Key={
#         'PK': 'CUSTOMER#itemtest',
#         'SK': 'PROFILE#itemtest'
#     })['Item']
#     assert request.text == item
