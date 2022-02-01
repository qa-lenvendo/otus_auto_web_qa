import pytest
from .test_data import sub_breed, breed_images


class TestApiDog:
    """
    Tests for API methods - `https://dog.ceo/dog-api/`
    """

    @pytest.mark.parametrize('test_input, expected', sub_breed, ids=[x[0] for x in sub_breed])
    def test_all_sub_breeds(self, api_dog, test_input, expected):
        response = api_dog.get_sub_breed_list(test_input).json()['message']
        assert response == expected

    @pytest.mark.parametrize('test_input, expected', breed_images, ids=[x[0] for x in breed_images])
    def test_by_breed_image(self, api_dog, test_input, expected):
        response = api_dog.get_by_breed(test_input).json()['message']
        assert response == expected

    def test_negative_by_breed_image(self, api_dog):
        test_input = 'invalid_type'
        response = api_dog.get_by_breed(test_input)
        assert response.status_code == 404

    @pytest.mark.parametrize('test_input, expected', breed_images, ids=[x[0] for x in breed_images])
    def test_random_breed_image(self, api_dog, test_input, expected):
        response = api_dog.get_random_breed_images(test_input).json()['message']
        assert response in expected

    def test_random_image_type(self, api_dog):
        response = api_dog.get_random_image().json()['message']
        assert isinstance(response, str)
