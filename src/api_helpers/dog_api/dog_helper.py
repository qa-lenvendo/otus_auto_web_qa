import requests
from jsonschema import validate
import os
import json


class DogHelper:

    def __init__(self, host):
        self.host = host
        self.request = requests.Session()
        self.valid_schema = self.load_schema('valid_schema')
        self.error_schema = self.load_schema('error_schema')

    def close(self):
        self.request.close()

    @staticmethod
    def load_schema(schema_name):
        schema_url = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{schema_name}.json')
        with open(schema_url) as f:
            schema = json.load(f)
        return schema

    def get(self, url, payload=None):
        """
        Отправка "Get" запроса и получение ответа.
        :param url: url для отправки запроса
        :param payload: параметры запроса
        :return: объект requests
        """
        r = self.request.get(url=url, params=payload)
        if r.status_code == 200:
            validate(instance=r.json(), schema=self.valid_schema)
        elif r.status_code == 404:
            validate(instance=r.json(), schema=self.error_schema)
        else:
            raise Exception(f'Непредвиденный ответ. Получен ответ с кодом "{r.status_code}"')

        return r

    def get_sub_breed_list(self, dog_type: str):
        """
        Получение списка пород собак по переданной породной группе собак.
        :param dog_type: породная группа собак, для которой необходимо получить список пород.
        :return: объект Response
        """
        return self.get(url=f'{self.host}/breed/{dog_type}/list')

    def get_random_image(self):
        """
        Получение изображения случайной собаки.
        :return: объект Response
        """
        return self.get(url=f'{self.host}/breeds/image/random')

    def get_by_breed(self, dog_type: str):
        """
        Получение списка изображений собак переданной породы.
        :param dog_type: Порода собак, для которой необходимо получить изображения.
        :return: объект Response
        """
        return self.get(url=f'{self.host}/breed/{dog_type}/images')

    def get_random_breed_images(self, dog_type: str):
        """
        Получение случайного изображения собаки переданной породы.
        :param dog_type: порода собак для которой необходимо получить изображение.
        :return: объект Response
        """
        return self.get(url=f'{self.host}/breed/{dog_type}/images/random')
