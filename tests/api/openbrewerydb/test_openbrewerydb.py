import random
import pytest
from .test_data import city_list, state_by_country


class TestApiDog:
    """
    Tests for API methods - `https://jsonplaceholder.typicode.com/`
    """

    def test_breweries_from_valid_data(self, api_openbrewerydb):
        response = api_openbrewerydb.get_breweries()
        assert response.status_code == 200

    def test_breweries_from_invalid_city(self, api_openbrewerydb):
        response = api_openbrewerydb.get_breweries(by_city=random.randrange(1, 10))
        assert len(response.json()) == 0

    @pytest.mark.parametrize('city', city_list)
    def test_breweries_by_city(self, api_openbrewerydb, city):
        response = api_openbrewerydb.get_breweries(by_city=city)
        for x in response.json():
            assert city in x['city']

    @pytest.mark.parametrize('state, country', state_by_country)
    def test_breweries_state_from_country(self, api_openbrewerydb, state, country):
        response = api_openbrewerydb.get_breweries(by_state=state)
        for x in response.json():
            assert x['country'] == country

    @pytest.mark.parametrize('postal_code', ['97703', '46534', '97701', '97703-2465'])
    def test_breweries_postal_code(self, api_openbrewerydb, postal_code):
        response = api_openbrewerydb.get_breweries(by_postal=postal_code)
        for x in response.json():
            assert postal_code in x['postal_code']
