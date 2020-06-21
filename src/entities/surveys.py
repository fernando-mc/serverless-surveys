import uuid


class NoCustomerIdException(Exception):
    pass


class Survey:
    """Deals with customer created surveys"""

    def __init__(self, customer_id=None, survey_id=None, survey_data=None):
        if customer_id is None:
            raise NoCustomerIdException("Surveys require a customer_id")

        self.customer_id = customer_id

        if survey_id:
            self.survey_id = survey_id
        else:
            self.survey_id = str(uuid.uuid4())
        if isinstance(survey_data, dict):
            self.survey_data = survey_data

    def key(self):
        return {
            'PK': f'CUSTOMER#{self.customer_id}',
            'SK': f'SURVEY#{self.survey_id}',
        }

    def to_item(self):
        return {
            **self.key(),
            "customer_id": self.customer_id,
            "survey_id": self.survey_id,
            "survey_data": self.survey_data
        }
