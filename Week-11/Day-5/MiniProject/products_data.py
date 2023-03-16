import json


def load_database(src_file='product_db.json'):
    with open(src_file, 'r') as file_obj:
        return json.load(file_obj)

