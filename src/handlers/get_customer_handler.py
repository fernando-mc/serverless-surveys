from lambda_decorators import (
    cors_headers, json_http_resp,
    json_schema_validator)
from src.entities.customers import Customer
from src.data.get_customer import get_customer


request_schema = {
    'type': 'object',
    'properties': {
        'pathParameters': {
            'type': 'object',
            'properties': {
                'customer_id': {'type': 'string'},
            },
            'required': ['customer_id']
        }
    },
    'required': ['pathParameters'],
}

@json_schema_validator(request_schema=request_schema)
@cors_headers
@json_http_resp
def handler(event, context):
    try:
        customer_id = event['pathParameters']['customer_id']
    except KeyError:
        raise Exception('customer_id is required in pathParameters')
    customer = Customer(customer_id=customer_id)
    result = get_customer(customer).to_item()
    if event.get('error'):
        raise Exception(event['error'])
    else:
        return result
