from src.data import create_survey

class StubSurvey:
    def to_item():
        return {
            "PK": "CUSTOMER#TEST1",
            "SK": "SURVEY#TEST1",
            "customer_id": "TEST1",
            "survey_id": "TEST1",
            "survey_data": {"TEST": "DATA"}
        }

def test_create_survey(dynamodb_table):
    assert create_survey.create_survey(survey=StubSurvey) == StubSurvey
