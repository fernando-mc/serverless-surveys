import pytest
import json
import src.entities.customers
import src.data.create_customer


class MockCustomer:
    pass


class Context:
    pass


good_event = {
    "body": json.dumps({
        "customer_id": "1",
        "profile_data": {
            "question1": "sup?"
        }
    })
}


@pytest.fixture(scope='function')
def setup_handler_monkeypatching(dynamodb_table, monkeypatch):
    def mock_customer(*args, **kwargs):
        return MockCustomer()

    def mock_create_customer(*args, **kwargs):
        pass
    monkeypatch.setattr(src.entities.customers, "Customer", mock_customer)
    monkeypatch.setattr(
        src.data.create_customer,
        "create_customer",
        mock_create_customer
    )


def test_create_customer_handler_has_cors_headers(setup_handler_monkeypatching):
    from src.handlers.create_customer_handler import handler
    result = handler(good_event, Context())
    assert result['headers'] == {'Access-Control-Allow-Origin': '*'}


def test_create_customer_handler_has_json_body(setup_handler_monkeypatching):
    from src.handlers.create_customer_handler import handler
    result = handler(good_event, Context)
    assert isinstance(json.loads(result['body']), dict)


def test_create_customer_handler_returns_schema_validation_error(setup_handler_monkeypatching):
    from src.handlers.create_customer_handler import handler
    result = handler({"bad_key": "bad_value"}, Context)
    assert result['statusCode'] == 400
    assert 'RequestValidationError' in result['body']
