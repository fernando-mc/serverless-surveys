from tests.utils.dynamodb import mocked_table


class StubSurvey:

    def __init__(self):
        pass

    def key(self):
        return {
            'PK': 'CUSTOMER#TEST_ID',
            'SK': 'SURVEY#TEST_ID'
        }


def test_get_survey(dynamodb_table):
    from src.data.get_survey import get_survey
    table = mocked_table()
    item = {
        'PK': 'CUSTOMER#TEST_ID',
        'SK': 'SURVEY#TEST_ID',
        'customer_id': 'TEST_ID',
        'survey_id': 'TEST_ID',
        'survey_data': {'some': 'data'}
    }
    table.put_item(Item=item)
    survey_instance = StubSurvey()
    assert get_survey(
        survey=survey_instance,
        table=table
    ).to_item() == item
