import pytest
from tests.utils.dynamodb import mocked_table


class StubResponse:

    def __init__(self):
        pass

    def to_item(self):
        return {
            'PK': 'SURVEY#TEST_SURVEY_ID',
            'SK': 'RESPONSE#TEST_RESPONSE_ID',
            'survey_id': 'TEST_SURVEY_ID',
            'response_id': 'TEST_RESPONSE_ID',
            'response_data': {'some': 'data'}
        }


def test_create_response(dynamodb_table):
    from src.data.create_response import create_response
    response_instance = StubResponse()
    table = mocked_table()
    assert create_response(
        response=response_instance,
        table=table
    ) == response_instance


def test_create_response_returns_error_info_when_it_fails(dynamodb_table):
    from src.data.create_response import (
        create_response, ResponseCreationException
    )
    table = mocked_table()
    with pytest.raises(ResponseCreationException):
        create_response(
            response='Garbage',
            table=table
        )
