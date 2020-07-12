from tests.utils.dynamodb import mocked_table

class StubResponse:

    def __init__(self):
        pass
    
    def key(self):
        return {
            'PK': 'SURVEY#TESTID',
            'SK': 'RESPONSE#TESTID'
        }


def test_get_response(dynamodb_table):
    from src.data.get_response import get_response
    table = mocked_table()
    item = {
        'PK': 'SURVEY#TESTID',
        'SK': 'RESPONSE#TESTID',
        'survey_id': 'TESTID',
        'response_id': 'TESTID',
        'response_data': {'some':'data'}
    }
    table.put_item(Item=item)
    response_instance = StubResponse()
    assert get_response(response=response_instance, table=table).to_item() == item
