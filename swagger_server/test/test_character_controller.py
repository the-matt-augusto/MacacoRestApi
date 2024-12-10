# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.character import Character  # noqa: E501
from swagger_server.models.images import Images  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCharacterController(BaseTestCase):
    """CharacterController integration test stubs"""

    def test_create_character(self):
        """Test case for create_character

        Add a new pet to the store
        """
        body = Character()
        data = dict(id='id_example',
                    name='name_example',
                    name_kanji='name_kanji_example',
                    nicknames='nicknames_example',
                    rarity=56,
                    gender='gender_example',
                    images=Images(),
                    media_id='media_id_example')
        response = self.client.open(
            '/character',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_character(self):
        """Test case for delete_character

        Deletes a pet
        """
        query_string = [('pet_id', 789)]
        response = self.client.open(
            '/character',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_character(self):
        """Test case for read_character

        List characters by filter
        """
        query_string = [('status', 'available')]
        response = self.client.open(
            '/character',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_character(self):
        """Test case for update_character

        Update an existing character
        """
        body = Character()
        data = dict(id='id_example',
                    name='name_example',
                    name_kanji='name_kanji_example',
                    nicknames='nicknames_example',
                    rarity=56,
                    gender='gender_example',
                    images=Images(),
                    media_id='media_id_example')
        response = self.client.open(
            '/character',
            method='PUT',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
