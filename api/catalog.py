import requests
import json
import pydash

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
                    raise Exception(f'Exception session_id not found in response')
            else:
                raise Exception(f'Exception auth is not success with message: {response.get("message")}')
        else:
            raise Exception(f'Exception with HTTP status code: {response.status_code}')

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
                raise Exception(f'Exception auth is not success with message: {response.get("message")}')
        else:
            raise Exception(f'Exception with HTTP status code: {response.status_code}')
