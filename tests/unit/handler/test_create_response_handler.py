import pytest
import json
import src.entities.responses
import src.data.create_response


class MockResponse:
    def to_result(self):
        return {'some': 'stuff'}


class Context:
    pass


good_event = {
    "body": json.dumps({
        "survey_id": "1",
        "response_id": "1",
        "response_data": {
            "responsestuff": "coolbeans"
        }
    })
}


@pytest.fixture(scope='function')
def setup_handler_monkeypatching(dynamodb_table, monkeypatch):
    def mock_response(*args, **kwargs):
        return MockResponse()

    def mock_create_response(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr(src.entities.responses, "Response", mock_response)
    monkeypatch.setattr(
        src.data.create_response,
        "create_response",
        mock_create_response
    )


def test_create_response_handler_returns_200(setup_handler_monkeypatching):
    from src.handlers.create_response_handler import handler
    result = handler(good_event, Context())
    assert result['statusCode'] == 200


def test_create_response_handler_has_cors_headers(setup_handler_monkeypatching):
    from src.handlers.create_response_handler import handler
    result = handler(good_event, Context())
    assert result['headers'] == {'Access-Control-Allow-Origin': '*'}


def test_create_response_handler_has_json_body(setup_handler_monkeypatching):
    from src.handlers.create_response_handler import handler
    result = handler(good_event, Context)
    assert isinstance(json.loads(result['body']), dict)


def test_create_response_handler_returns_schema_validation_error(setup_handler_monkeypatching):
    from src.handlers.create_response_handler import handler
    result = handler({"bad_key": "bad_value"}, Context)
    assert result['statusCode'] == 400
    assert 'RequestValidationError' in result['body']
