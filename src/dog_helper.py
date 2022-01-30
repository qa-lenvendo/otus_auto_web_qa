import requests
from jsonschema import validate


class DogHelper:

    def __init__(self, host):
        self.host = host
        self.request = requests.Session()

    def close(self):
        self.request.close()

    def get_sub_breed_list(self, dog_type):
        response = self.request.get(url=f'{self.host}/breed/{dog_type}/list')

        schema = {
            "type": "object",
            "properties": {
                "message": {"type": "array"},
                "status": {"type": "string"}
            },
            "required": ["message", "status"]
        }

        validate(instance=response.json(), schema=schema)

        return response

    def get_random_image(self):
        response = self.request.get(url=f'{self.host}/breeds/image/random')

        schema = {
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "status": {"type": "string"}
            },
            "required": ["message", "status"]
        }

        validate(instance=response.json(), schema=schema)

        return response

    def get_by_breed(self, dog_type):
        response = self.request.get(url=f'{self.host}/breed/{dog_type}/images')

        if response.status_code == 200:
            schema = {
                "type": "object",
                "properties": {
                    "message": {"type": "array"},
                    "status": {"type": "string"}
                },
                "required": ["message", "status"]
            }

            validate(instance=response.json(), schema=schema)

        else:
            schema = {
                "type": "object",
                "properties": {
                    "status": {"type": "string"},
                    "message": {"type": "string"},
                    "code": {"type": "integer"}
                },
                "required": ["status", "message", "code"]
            }

            validate(instance=response.json(), schema=schema)

        return response

    def get_random_breed_images(self, dog_type):
        response = self.request.get(url=f'{self.host}/breed/{dog_type}/images/random')

        schema = {
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "status": {"type": "string"}
            },
            "required": ["message", "status"]
        }

        validate(instance=response.json(), schema=schema)

        return response
