from lambda_decorators import (
    cors_headers, json_http_resp,
    json_schema_validator, dump_json_body)
from src.entities.customers import Customer
from src.data.get_all_customer_surveys import get_all_customer_surveys


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
    all_surveys_result = get_all_customer_surveys(customer)
    if hasattr(all_surveys_result, 'error'):
        raise Exception(all_surveys_result['error'])
    surveys = []
    for survey in all_surveys_result:
        surveys.append(survey.to_result())
    return {'surveys': surveys}
