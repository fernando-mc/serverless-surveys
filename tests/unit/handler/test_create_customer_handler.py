import json


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


def test_create_customer_handler_returns_200(dynamodb_table):
    from src.handlers.create_customer_handler import handler
    result = handler(good_event, Context())
    assert result['statusCode'] == 200


def test_create_customer_handler_has_cors_headers(dynamodb_table):
    from src.handlers.create_customer_handler import handler
    result = handler(good_event, Context())
    assert result['headers'] == {'Access-Control-Allow-Origin': '*'}


def test_create_customer_handler_has_json_body(dynamodb_table):
    from src.handlers.create_customer_handler import handler
    result = handler(good_event, Context)
    assert isinstance(json.loads(result['body']), dict)


def test_create_customer_handler_returns_schema_validation_error(dynamodb_table):
    from src.handlers.create_customer_handler import handler
    result = handler({"bad_key": "bad_value"}, Context)
    assert result['statusCode'] == 400
    assert 'RequestValidationError' in result['body']
