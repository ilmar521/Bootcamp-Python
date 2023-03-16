import json


def load_database(src_file='product_db.json'):
    with open(src_file, 'r') as file_obj:
        data = json.load(file_obj) # you can just do return at this line, like: return json.load(file_obj)
    return data
