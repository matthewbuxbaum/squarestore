from square.client import Client
from pprint import pprint


# Create an instance of the API Client
# and initialize it with the credentials
# for the Square account whose assets you want to manage

def get_categories(client):
    category_list = []
    result = client.catalog.list_catalog(
        types="category"
    )

    if result.is_success():
        json_result = result.body
        category_objects = json_result['objects']
        for category in category_objects:
            category_name = category['category_data'].get('name')
            category_id = category.get('id')
            category_dictionary = {'category_name': category_name, 'category_id': category_id}
            category_list.append(category_dictionary)
    elif result.is_error():
        print(result.errors)
    return category_list


def get_images(client):
    image_list = []
    result = client.catalog.list_catalog(
        types="image"
    )

    if result.is_success():
        json_result = result.body
        image_objects = json_result['objects']
        for image in image_objects:
            image_id = image.get('id')
            image_url = image['image_data'].get('url')
            image_dictionary = {'image_id': image_id, 'image_url': image_url}
            image_list.append(image_dictionary)
    elif result.is_error():
        print(result.errors)
    return image_list


def get_items(client):
    item_list = []
    result = client.catalog.list_catalog(
        types="item"
    )
    if result.is_success():
        json_result = result.body
        item_objects = json_result['objects']
        for item in item_objects:
            item_variation_list = []
            item_image_id = item.get('image_id')
            item_category_id = item['item_data'].get('category_id')
            item_name = item['item_data'].get('name')
            for variation in item['item_data']['variations']:
                item_variation_name = variation['item_variation_data'].get('name')
                item_viariation_price = variation['item_variation_data']['price_money'].get('amount')
                item_variation_dictionary = {'name': item_variation_name, 'price': item_viariation_price}
                item_variation_list.append(item_variation_dictionary)
            for key in item['item_data'].keys():
                if key == 'modifier_list_info':
                    item_modifier_list_id = item['item_data']['modifier_list_info'][0]['modifier_list_id']
            item_dictionary = {'item_name': item_name, 'item_category_id': item_category_id,
                               'item_image_id': item_image_id, 'item_modifier_list_id': item_modifier_list_id, 'item_variation': item_variation_list}
            item_list.append(item_dictionary)
    elif result.is_error():
        print(result.errors)
    return item_list


def get_modifiers(client):
    modifier_list = []
    result = client.catalog.list_catalog(
        types="modifier_list"
    )

    if result.is_success():
        json_result = result.body
        modifier_objects = json_result['objects']
        for modifier in modifier_objects:
            modifier_info_list = []
            modifier_set_name = modifier['modifier_list_data'].get('name')
            for modifier_info in modifier['modifier_list_data']['modifiers']:
                modifier_name = modifier_info['modifier_data']['name']
                modifier_list_id = modifier_info['modifier_data']['modifier_list_id']
                modifier_info_dictionary = {'modifier_name': modifier_name, 'modifier_list_id': modifier_list_id}
                modifier_info_list.append(modifier_info_dictionary)
            modifier_dictionary = {'modifier_set_name': modifier_set_name, 'modifier_info': modifier_info_list}
            modifier_list.append(modifier_dictionary)
    elif result.is_error():
        print(result.errors)
    return modifier_list


def join_catalog(client, categories, images, items, modifiers):
    catalog_list = []
    for item in items:
        modifier_list = []
        for category in categories:
            if item.get('item_category_id') == category.get('category_id'):
                category_name = category.get('category_name')
        for image in images:
            if item.get('item_image_id') == image.get('image_id'):
                item_image_url = image.get('image_url')
        for modifier in modifiers:
            # print(modifier)
            modifier_name_list = []
            modifier_set_name = modifier['modifier_set_name']
            for modifier_info in modifier['modifier_info']:
                # print(modifier_info)
                # print(modifier_info.get('modifier_list_id'))
                if item.get('item_modifier_list_id') == modifier_info.get('modifier_list_id'):
                    modifier_name = modifier_info.get('modifier_name')
                    modifier_name_list.append(modifier_name)
            modifier_catalog_dictionary = {'modifier_set_name': modifier_set_name, 'modifier_name': modifier_name_list}
            modifier_list.append(modifier_catalog_dictionary)
        catalog_dictionary = {'item_name': item.get('item_name'), 'item_category': category_name,
                              'item_image_url': item_image_url, 'item_variation': item['item_variation'],
                              'modifiers': modifier_list}
        catalog_list.append(catalog_dictionary)
    return catalog_list


if __name__ == '__main__':
    client = Client(
        access_token='EAAAECjv361sFnMkIAHZjjaBhZEGEsn2lSnWqFUyYzG2SR2tPzPr713RsxlebQ4J',
        environment='sandbox'
    )

    categories = get_categories(client)
    images = get_images(client)
    items = get_items(client)
    modifiers = get_modifiers(client)
    # pprint(modifiers)
    catalog = join_catalog(client, categories, images, items, modifiers)
    pprint(catalog)
