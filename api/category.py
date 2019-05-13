import requests
import json
import os

from settings import IT_PARTNET_CATEGORY_URL, BASE_PATH

class CategoryApi:

    @staticmethod
    def get_all():
        response = requests.get(IT_PARTNET_CATEGORY_URL)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception(f'HTTP status code: {response.status_code}')

    @staticmethod
    def get_test():
        with open(os.path.join(BASE_PATH, 'api', 'catalog_tree.json')) as file:
            return json.loads(file.read())
        return []
