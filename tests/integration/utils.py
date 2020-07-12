import boto3


def get_endpoint_url(service_name, stage):
    """Get APIGateway endpoint URL."""
    cloudformation = boto3.client('cloudformation')
    stackname = '{}-{}'.format(service_name, stage)
    response = cloudformation.describe_stacks(
        StackName=stackname
    )
    for output in response['Stacks'][0]['Outputs']:
        if output['OutputKey'] == 'ServiceEndpoint':
            return output['OutputValue']
