from lambda_decorators import (
    load_json_body, json_schema_validator,
    cors_headers, json_http_resp, dump_json_body)
from src.entities.responses import Response
from src.data.create_response import create_response

request_schema = {
    'type': 'object',
    'properties': {
        'body': {
            'type': 'object',
            'properties': {
                'survey_id': {'type': 'string'},
                'response_data': {'type': 'object'}
            },
            'required': ['survey_id', 'response_data']
        }
    },
    'required': ['body'],
}


@load_json_body  # Doing this first is required for the schema to validate
@json_schema_validator(request_schema=request_schema)
@cors_headers
@json_http_resp
@dump_json_body
def handler(event, context):
    response = Response(**event['body'])
    result = create_response(response)
    if hasattr(result, 'error'):
        raise Exception(result['error'])
    else:
        return result.to_result()
