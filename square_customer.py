from square.client import Client
from pprint import pprint
# Create an instance of the API Client
# and initialize it with the credentials
# for the Square account whose assets you want to manage

client = Client(
    access_token='EAAAECjv361sFnMkIAHZjjaBhZEGEsn2lSnWqFUyYzG2SR2tPzPr713RsxlebQ4J',
    environment='sandbox'
)

def create_client(client, ):
    result = client.customers.create_customer(
      body = {
        "given_name": "Amelia",
        "family_name": "Earhart",
        "email_address": "Amelia.Earhart@example.com",
        "address": {
          "address_line_1": "500 Electric Ave",
          "address_line_2": "Suite 600",
          "locality": "New York",
          "administrative_district_level_1": "NY",
          "postal_code": "10003",
          "country": "US"
        },
        "phone_number": "1-212-555-4240",
        "reference_id": "YOUR_REFERENCE_ID",
        "note": "a customer"
      }
    )

    if result.is_success():
      pprint(result.body)
    elif result.is_error():
      print(result.errors)

def get_customer(client):
    result = client.customers.list_customers()

    if result.is_success():
        pprint(result.body)
    elif result.is_error():
        print(result.errors)

if __name__ == '__main__':
    get_customer(client)

