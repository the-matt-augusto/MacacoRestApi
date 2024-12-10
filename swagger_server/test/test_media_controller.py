# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.media import Media  # noqa: E501
from swagger_server.models.title import Title  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMediaController(BaseTestCase):
    """MediaController integration test stubs"""

    def test_create_media(self):
        """Test case for create_media

        Place an order for a pet
        """
        body = Media()
        data = dict(id='id_example',
                    title=Title())
        response = self.client.open(
            '/media',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_media(self):
        """Test case for delete_media

        Place an order for a pet
        """
        response = self.client.open(
            '/media',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_media(self):
        """Test case for get_media

        Place an order for a pet
        """
        response = self.client.open(
            '/media',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_media(self):
        """Test case for update_media

        Place an order for a pet
        """
        body = Media()
        data = dict(id='id_example',
                    title=Title())
        response = self.client.open(
            '/media',
            method='PUT',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
