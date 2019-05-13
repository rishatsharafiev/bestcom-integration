import requests
import json
import pydash
import time

from settings import IT_PARTNET_API_URL, BASE_PATH

class CatalogApi:

    @staticmethod
    def auth(login: str, password: str):
        data = {
            "data": {
                "login": login,
                "passwd": password
            },
            "request": {
                "method": "login",
                "module": "system"
            }
        }

        response = requests.post(IT_PARTNET_API_URL, json=data)

        # ограничение 10 запросов в минуту
        # import time
        # time.sleep(6)

        if response.status_code == 200:
            response = json.loads(response.text)

            if response.get('success'):
                session_id = pydash.get(response, 'data.session_id')
    
                if session_id:                    
                    return session_id
                else:
                    raise Exception(f'session_id not found in response')
            else:
                raise Exception(f'auth is not success with message: "{response.get("message")}"')
        else:
            raise Exception(f'HTTP status code: {response.status_code}')

    @staticmethod
    def get_active_products(session_id: str):
        data = {
            "request": {
                "method": "get_active_products",
                "model": "client_api",
                "module": "platform"
            },
            "session_id": session_id
        }

        response = requests.post(IT_PARTNET_API_URL, json=data)

        # ограничение 10 запросов в час
        # import time
        # time.sleep(36)

        if response.status_code == 200:
            response = json.loads(response.text)

            if response.get('success'):
                return pydash.get(response, 'data.products', [])
            else:
                raise Exception(f'request is not success with message: {response.get("message")}')
        else:
            raise Exception(f'HTTP status code: {response.status_code}')

    @staticmethod
    def get_products_clients_images(session_id: str, sku: str):
        data = {
            "filter": [
                {
                    "operator": "=",
                    "property": "sku",
                    "value": sku
                },
                {
                    "operator": "=",
                    "property": "type",
                    "value": 3
                }
            ],
            "request": {
                "method": "read",
                "model": "products_clients_images",
                "module": "platform"
            },
            "session_id": session_id
        }

        response = requests.post(IT_PARTNET_API_URL, json=data)

        # ограничение 10 запросов в секунду
        # import time
        time.sleep(0.2)

        if response.status_code == 200:
            response = json.loads(response.text)

            if response.get('success'):
                return pydash.get(response, 'data.products_clients_images', [])
            else:
                raise Exception(f'request is not success with message: {response.get("message")}')
        else:
            raise Exception(f'HTTP status code: {response.status_code} with sku: {sku}')
