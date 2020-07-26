from lambda_decorators import (
    cors_headers, json_http_resp,
    json_schema_validator, dump_json_body)
from src.entities.responses import Response
from src.data.get_response import get_response


request_schema = {
    'type': 'object',
    'properties': {
        'pathParameters': {
            'type': 'object',
            'properties': {
                'survey_id': {'type': 'string'},
                'response_id': {'type': 'string'},
            },
            'required': ['survey_id', 'response_id']
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
    response_id = event['pathParameters']['response_id']
    response = Response(survey_id=survey_id, response_id=response_id)
    result = get_response(response)
    if hasattr(result, 'error'):
        raise Exception(result['error'])
    return result.to_result()
