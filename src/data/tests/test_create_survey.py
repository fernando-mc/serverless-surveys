from src.data.create_survey import create_survey


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


def test_create_survey(dynamodb_table):
    survey_instance = StubSurvey()
    assert create_survey(survey=survey_instance) == survey_instance
