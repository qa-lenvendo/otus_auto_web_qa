import requests
from jsonschema import validate


class JsonPlaceholderHelper:

    def __init__(self, host):
        self.host = host
        self.request = requests.Session()

    def close(self):
        self.request.close()

    def get_posts(self, user_id=None, id=None, title=None):
        payload = {"userId": user_id, "id": id, "title": title}
        response = self.request.get(url=f'{self.host}/posts', params=payload)

        schema = {
            "type": "array",
            "properties": {
                "userId": {"type": "integer"},
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "body": {"type": "string"}
            },
            "required": ["userId", "id", "title", "body"]
        }

        validate(instance=response.json(), schema=schema)

        return response
