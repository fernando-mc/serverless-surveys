from lambda_decorators import (
    load_json_body, json_schema_validator,
    cors_headers, json_http_resp)
from src.entities.surveys import Survey
from src.data.create_survey import create_survey

request_schema = {
    'type': 'object',
    'properties': {
        'body': {
            'type': 'object',
            'properties': {
                'customer_id': {'type': 'string'},
                'survey_id': {'type:': 'string'},
                'survey_data': {'type': 'object'}
            },
            'required': ['customer_id', 'survey_data']
        }
    },
    'required': ['body'],
}


@load_json_body  # Doing this first is required for the schema to validate
@json_schema_validator(request_schema=request_schema)
@cors_headers
@json_http_resp
def handler(event, context):
    survey = Survey(**event['body'])
    create_survey(survey)
    if event.get('error'):
        raise Exception(event['error'])
    else:
        return event['body']
