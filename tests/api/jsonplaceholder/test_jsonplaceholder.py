import random

import pytest
from .test_data import user_posts, post_ids


class TestApiDog:
    """
    Tests for API methods - `https://jsonplaceholder.typicode.com/`
    """

    @pytest.mark.parametrize('user_id', [x + 1 for x in range(10)])
    def test_user_id_filter(self, api_jsonplaceholder, user_id):
        response = api_jsonplaceholder.get_posts(user_id=user_id).json()
        for x in response:
            assert x['userId'] == user_id

    @pytest.mark.parametrize('user_post', user_posts)
    def test_post_id_for_users(self, api_jsonplaceholder, user_post):
        response = api_jsonplaceholder.get_posts(id=user_post[0]).json()
        for x in response:
            assert x['userId'] == user_post[1]

    @pytest.mark.parametrize('post_id, post_title', post_ids)
    def test_title_post_for_post_id(self, api_jsonplaceholder, post_id, post_title):
        response = api_jsonplaceholder.get_posts(id=post_id).json()
        for x in response:
            assert x['title'] == post_title

    def test_empty_list_max_user_id(self, api_jsonplaceholder):
        response = api_jsonplaceholder.get_posts(user_id=random.randrange(101, 1000)).json()
        assert len(response) == 0

    @pytest.mark.parametrize('user_id', [x + 1 for x in range(10)])
    def test_response_status_for_all_user_id(self, api_jsonplaceholder, user_id):
        response = api_jsonplaceholder.get_posts(user_id=user_id)
        assert response.status_code == 200
