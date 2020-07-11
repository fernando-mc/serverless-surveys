from tests.utils.dynamodb import mocked_table

class StubResponse:

    def __init__(self):
        pass
    
    def to_item(self):
        return {
            'PK': 'SURVEY#TESTSURVEYID',
            'SK': 'RESPONSE#TESTRESPONSEID',
            'survey_id': 'TESTSURVEYID',
            'response_id': 'TESTRESPONSEID',
            'response_data': {'some':'data'}
        }


def test_create_customer(dynamodb_table):
    from src.data.create_response import create_response
    response_instance = StubResponse()
    table = mocked_table()
    assert create_response(response=response_instance, table=table) == response_instance
