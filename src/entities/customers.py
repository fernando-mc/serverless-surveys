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


def customer_from_item(attributes):
    return Customer(
        customer_id=attributes['customer_id'],
        profile_data=attributes['profile_data'],
    )
