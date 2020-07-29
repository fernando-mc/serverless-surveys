import os
import boto3


def get_rest_endpoint_url(service_name, stage):
    """Get API Gateway REST API endpoint URL."""
    cloudformation = boto3.client('cloudformation')
    stackname = '{}-{}'.format(service_name, stage)
    response = cloudformation.describe_stacks(
        StackName=stackname
    )
    for output in response['Stacks'][0]['Outputs']:
        if output['OutputKey'] == 'ServiceEndpoint':
            return output['OutputValue']


def get_http_api_endpoint_url(service_name, stage):
    """Get API Gateway HTTP API endpoint URL."""
    cloudformation = boto3.client('cloudformation')
    stackname = '{}-{}'.format(service_name, stage)
    response = cloudformation.describe_stacks(
        StackName=stackname
    )
    for output in response['Stacks'][0]['Outputs']:
        if output['OutputKey'] == 'HttpApiUrl':
            return output['OutputValue']


def get_client_id():
    return 'usJS7BooZsSBTOEconsiuYKeNMoYGlrb'


def get_auth0_bearer_token():
    import requests
    payload = {
        'client_id': get_client_id(),
        'client_secret': os.environ['TEST_AUTH0_CLIENT_SECRET'],
        'audience': 'serverless-surveys',
        'grant_type': 'client_credentials'
    }
    url = 'https://dev-5xmirf9t.auth0.com/oauth/token'
    response = requests.post(url, json=payload)
    return response.json()['access_token']
