class StubSurvey:

    def __init__(self):
        pass
    
    def to_item(self):
        return {
            "PK": "CUSTOMER#TEST1",
            "SK": "SURVEY#TEST1",
            "customer_id": "TEST1",
            "survey_id": "TEST1",
            "survey_data": {"TEST": "DATA"}
        }


def mocked_table():
    import boto3
    import os
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table


def test_create_survey(dynamodb_table):
    from src.data.create_survey import create_survey
    survey_instance = StubSurvey()
    table = mocked_table()
    assert create_survey(survey=survey_instance, table=table) == survey_instance
