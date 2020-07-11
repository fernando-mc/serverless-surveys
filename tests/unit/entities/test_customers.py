import pytest
import re
from src.entities.customers import Customer, NoCustomerIdException


def test_instantiating_customer_class_with_valid_data():
    customer_id = '1'
    profile_data = {'key': 'value'}
    customer = Customer(customer_id=customer_id, profile_data=profile_data)

    assert customer.customer_id == customer_id
    assert customer.profile_data == profile_data


def test_instantiating_customer_with_blank_customer_id_fails():
    with pytest.raises(NoCustomerIdException):
        Customer()


def test_customer_key():
    customer_id = 'TESTID'
    customer = Customer(
        customer_id=customer_id,
        profile_data=None
    )
    test_key = {
        'PK': 'CUSTOMER#TESTID',
        'SK': 'PROFILE#TESTID'
    }
    assert isinstance(customer.key(), dict)
    assert customer.key() == test_key


def test_to_item_serialization():
    customer_id = 'TESTID'
    profile_data = {'profile': 'data'}
    customer = Customer(
        customer_id=customer_id,
        profile_data=profile_data
    )
    test_item = {
        'PK': 'CUSTOMER#TESTID',
        'SK': 'PROFILE#TESTID',
        'customer_id': 'TESTID',
        'profile_data': profile_data
    }
    assert isinstance(customer.to_item(), dict)
    assert customer.to_item() == test_item
