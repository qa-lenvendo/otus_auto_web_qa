import requests
from jsonschema import validate


class OpenBreweryDb:

    def __init__(self, host):
        self.host = host
        self.request = requests.Session()

    def close(self):
        self.request.close()

    def get_breweries(self, by_city=None, by_state=None, by_postal=None):
        payload = {"by_city": by_city, "by_state": by_state, "by_postal": by_postal}
        response = self.request.get(url=f'{self.host}/breweries', params=payload)

        schema = {
            "type": "array",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": "string"},
                "address_2": {"type": "null"},
                "address_3": {"type": "null"},
                "city": {"type": "string"},
                "state": {"type": "string"},
                "county_province": {"type": "null"},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": "string"},
                "latitude": {"type": "string"},
                "phone": {"type": "string"},
                "website_url": {"type": "string"},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "address_2", "address_3", "city", "state",
                         "county_province", "postal_code", "country", "longitude", "latitude", "phone", "website_url",
                         "updated_at", "created_at"]
        }

        validate(instance=response.json(), schema=schema)

        return response
