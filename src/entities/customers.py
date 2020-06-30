import boto3
import json
import os
import uuid


class NoCustomerIdException(Exception):
    pass


class Customer:
    def __init__(self, customer_id=None, profile_data=None):
        if customer_id is None:
            raise NoCustomerIdException("Customers require a customer_id")

        self.customer_id = customer_id

        if isinstance(profile_data, dict):
            self.profile_data = profile_data

    def key(self):
        return {
            'PK': f'CUSTOMER#{self.customer_id}',
            'SK': f'PROFILE#{self.customer_id}',
        }

    def to_item(self):
        return {
            **self.key(),
            "customer_id": self.customer_id,
            "profile_data": self.profile_data
        }


    def get(event, body):
        print(event)
        customer_id = event['pathParameters']['id']
        item = table.get_item(
            Key={
                'pk': 'CUSTOMER#' + customer_id,
                'sk': 'PROFILE#' + customer_id
            }
        )['Item']
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
