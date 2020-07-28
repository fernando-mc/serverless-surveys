from lambda_decorators import (
    cors_headers, json_http_resp,
    json_schema_validator, dump_json_body)
from src.entities.customers import Customer
from src.data.get_customer import get_customer


request_schema = {
    'type': 'object',
    'properties': {
        'requestContext': {
            'type': 'object',
            'properties': {
                'authorizer': {'type': 'object'}
            }
        }
    },
    'required': ['requestContext'],
}


@json_schema_validator(request_schema=request_schema)
@cors_headers
@json_http_resp
@dump_json_body
def handler(event, context):
    sub = event['requestContext']['authorizer']['jwt']['claims']['sub']
    customer = Customer(customer_id=sub)
    result = get_customer(customer)
    if hasattr(result, 'error'):
        raise Exception(result['error'])
    return result.to_result()
