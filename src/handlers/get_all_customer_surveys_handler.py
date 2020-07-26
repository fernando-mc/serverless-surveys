from lambda_decorators import (
    cors_headers, json_http_resp,
    json_schema_validator, dump_json_body)
from src.entities.customers import Customer
from src.data.get_all_customer_surveys import get_all_customer_surveys


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
@dump_json_body
def handler(event, context):
    customer_id = event['pathParameters']['customer_id']
    customer = Customer(customer_id=customer_id)
    all_surveys_result = get_all_customer_surveys(customer)
    if hasattr(all_surveys_result, 'error'):
        raise Exception(all_surveys_result['error'])
    surveys = []
    for survey in all_surveys_result:
        surveys.append(survey.to_result())
    return {'surveys': surveys}
