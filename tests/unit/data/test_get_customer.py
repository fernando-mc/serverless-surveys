from tests.utils.dynamodb import mocked_table


class StubCustomer:

    def __init__(self):
        pass

    def key(self):
        return {
            'PK': 'CUSTOMER#TEST_ID',
            'SK': 'PROFILE#TEST_ID'
        }


def test_get_customer(dynamodb_table):
    from src.data.get_customer import get_customer
    table = mocked_table()
    item = {
        'PK': 'CUSTOMER#TEST_ID',
        'SK': 'PROFILE#TEST_ID',
        'customer_id': 'TEST_ID',
        'profile_data': {'some': 'data'}
    }
    table.put_item(Item=item)
    customer_instance = StubCustomer()
    assert get_customer(
        customer=customer_instance,
        table=table
    ).to_item() == item
