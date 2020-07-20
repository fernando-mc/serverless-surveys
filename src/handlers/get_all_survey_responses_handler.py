from lambda_decorators import (
    cors_headers, json_http_resp,
    json_schema_validator, dump_json_body)
from src.entities.surveys import Survey
from src.data.get_all_survey_responses import get_all_survey_responses


request_schema = {
    'type': 'object',
    'properties': {
        'pathParameters': {
            'type': 'object',
            'properties': {
                'survey_id': {'type': 'string'},
            },
            'required': ['survey_id']
        }
    },
    'required': ['pathParameters'],
}


@json_schema_validator(request_schema=request_schema)
@cors_headers
@json_http_resp
@dump_json_body
def handler(event, context):
    survey_id = event['pathParameters']['survey_id']
    survey = Survey(survey_id=survey_id)
    all_responses_result = get_all_survey_responses(survey)
    if hasattr(all_responses_result, 'error'):
        raise Exception(all_responses_result['error'])
    else:
        responses = []
        for response in all_responses_result:
            responses.append(response.to_result())
        return {'responses': responses}
