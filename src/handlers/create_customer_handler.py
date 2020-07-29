from lambda_decorators import (
    load_json_body, json_schema_validator,
    cors_headers, json_http_resp, dump_json_body)
from src.entities.customers import Customer
from src.data.create_customer import create_customer

request_schema = {
    'type': 'object',
    'properties': {
        'body': {
            'type': 'object',
            'properties': {
                'profile_data': {'type': 'object'}
            },
            'required': ['profile_data']
        },
        'requestContext': {
            'type': 'object',
            'properties': {
                'authorizer': {'type': 'object'}
            }
        }
    },
    'required': ['body', 'requestContext'],
}


@load_json_body  # Doing this first is required for the schema to validate
@json_schema_validator(request_schema=request_schema)
@cors_headers
@json_http_resp
@dump_json_body
def handler(event, context):
    sub = event['requestContext']['authorizer']['jwt']['claims']['sub']
    body = event['body']
    body['customer_id'] = sub
    customer = Customer(**event['body'])
    result = create_customer(customer)
    if hasattr(result, 'error'):
        raise Exception(result['error'])
    return result.to_result()
