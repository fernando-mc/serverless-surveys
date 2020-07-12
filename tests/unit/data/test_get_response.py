from tests.utils.dynamodb import mocked_table


class StubResponse:

    def __init__(self):
        pass

    def key(self):
        return {
            'PK': 'SURVEY#TEST_ID',
            'SK': 'RESPONSE#TEST_ID'
        }


def test_get_response(dynamodb_table):
    from src.data.get_response import get_response
    table = mocked_table()
    item = {
        'PK': 'SURVEY#TEST_ID',
        'SK': 'RESPONSE#TEST_ID',
        'survey_id': 'TEST_ID',
        'response_id': 'TEST_ID',
        'response_data': {'some': 'data'}
    }
    table.put_item(Item=item)
    response_instance = StubResponse()
    assert get_response(
        response=response_instance,
        table=table
    ).to_item() == item
