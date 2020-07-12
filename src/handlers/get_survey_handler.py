from lambda_decorators import (
    cors_headers, json_http_resp,
    json_schema_validator)
from src.entities.surveys import Survey
from src.data.get_survey import get_survey


request_schema = {
    'type': 'object',
    'properties': {
        'pathParameters': {
            'type': 'object',
            'properties': {
                'customer_id': {'type': 'string'},
                'survey_id': {'type': 'string'},
            },
            'required': ['customer_id', 'survey_id']
        }
    },
    'required': ['pathParameters'],
}


@json_schema_validator(request_schema=request_schema)
@cors_headers
@json_http_resp
def handler(event, context):
    customer_id = event['pathParameters']['customer_id']
    survey_id = event['pathParameters']['survey_id']
    survey = Survey(customer_id=customer_id, survey_id=survey_id)
    result = get_survey(survey).to_item()
    if event.get('error'):
        raise Exception(event['error'])
    else:
        return result
