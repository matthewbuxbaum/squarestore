from square.client import Client
from pprint import pprint
# Create an instance of the API Client
# and initialize it with the credentials
# for the Square account whose assets you want to manage

client = Client(
    access_token='EAAAECjv361sFnMkIAHZjjaBhZEGEsn2lSnWqFUyYzG2SR2tPzPr713RsxlebQ4J',
    environment='sandbox'
)


# result = client.catalog.retrieve_catalog_object(
#   object_id = "YZMP2CYJMFSUSTXL5GLGK5TQ",
#   include_related_objects = True
# )
#
# if result.is_success():
#   pprint(result.body)
# elif result.is_error():
#   print(result.errors)
# Get an instance of the Square API you want call
# api_locations = client.locations

# Call list_locations method to get all locations in this Square account
# result = api_locations.list_locations()
# result = client.catalog.list_catalog(types='category,tax,item')
# if result.is_success():
#   print(result.body)
# elif result.is_error():
#   print(result.errors)
# Call the success method to see if the call succeeded
# if result.is_success():
#     # The body property is a list of locations
#     locations = result.body['locations']
#     # Iterate over the list
#     for location in locations:
#         # Each location is represented as a dictionary
#         for key, value in location.items():
#             print(f"{key} : {value}")
#         print("\n")
# # Call the error method to see if the call failed
# elif result.is_error():
#     print('Error calling LocationsApi.listlocations')
#     errors = result.errors
#     # An error is returned as a list of errors
#     for error in errors:
#         # Each error is represented as a dictionary
#         for key, value in error.items():
#             print(f"{key} : {value}")
#         print("\n")


