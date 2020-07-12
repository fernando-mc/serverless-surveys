import uuid


class NoSurveyIdException(Exception):
    pass


class Response:
    """Deals with survey responses"""

    def __init__(self, survey_id=None, response_id=None, response_data=None):
        if survey_id is None:
            raise NoSurveyIdException("Responses require a survey_id")

        self.survey_id = survey_id

        if response_id:
            self.response_id = response_id
        else:
            self.response_id = str(uuid.uuid4())

        if isinstance(response_data, dict):
            self.response_data = response_data

    def key(self):
        return {
            'PK': f'SURVEY#{self.survey_id}',
            'SK': f'RESPONSE#{self.response_id}',
        }

    def to_item(self):
        return {
            **self.key(),
            "survey_id": self.survey_id,
            "response_id": self.response_id,
            "response_data": self.response_data
        }


def response_from_item(attributes):
    return Response(
        survey_id=attributes['survey_id'],
        response_id=attributes['response_id'],
        response_data=attributes['response_data']
    )
