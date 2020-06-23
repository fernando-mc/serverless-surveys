import pytest
import json
import src.entities.surveys
import src.data.create_survey

class MockSurvey:
    pass

class Context:
    pass

good_event = {
    "body": json.dumps({
        "customer_id": "1",
        "survey_id": "1",
        "survey_data": {
            "question1": "sup?"
        }
    })
}

@pytest.fixture(scope='function')
def setup_handler_monkeypatching(dynamodb_table, monkeypatch):
    def mock_survey(*args, **kwargs):
        return MockSurvey()

    def mock_create_survey(*args, **kwargs):
        pass
    monkeypatch.setattr(src.entities.surveys, "Survey", mock_survey)
    monkeypatch.setattr(src.data.create_survey, "create_survey", mock_create_survey)
    

def test_create_survey_handler_has_cors_handlers(setup_handler_monkeypatching):
    from src.handlers.create_survey_handler import handler
    result = handler(good_event, Context())
    assert result['headers'] == {'Access-Control-Allow-Origin': '*'}


def test_create_survey_handler_has_json_body(setup_handler_monkeypatching):
    from src.handlers.create_survey_handler import handler
    result = handler(good_event, Context)
    assert isinstance(json.loads(result['body']), dict)

def test_create_survey_handler_returns_schema_validation_error(setup_handler_monkeypatching):
    from src.handlers.create_survey_handler import handler
    result = handler({"bad_key": "bad_value"}, Context)
    assert result['statusCode'] == 400
    assert 'RequestValidationError' in result['body']
