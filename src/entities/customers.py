class NoCustomerIdException(Exception):
    pass


class Customer:
    def __init__(self, customer_id=None, profile_data=None):
        if customer_id is None:
            raise NoCustomerIdException("Customers require a customer_id")

        self.customer_id = customer_id

        if isinstance(profile_data, dict):
            self.profile_data = profile_data

    def pk(self):
        return f'CUSTOMER#{self.customer_id}'

    def key(self):
        return {
            'PK': self.pk(),
            'SK': f'PROFILE#{self.customer_id}',
        }

    def to_result(self):
        return {
            "customer_id": self.customer_id,
            "profile_data": self.profile_data
        }

    def to_item(self):
        return {
            **self.key(),
            **self.to_result()
        }


def customer_from_item(attributes):
    return Customer(
        customer_id=attributes['customer_id'],
        profile_data=attributes['profile_data'],
    )
