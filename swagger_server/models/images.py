# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Images(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, image_url: str=None, small_image_url: str=None):  # noqa: E501
        """Images - a model defined in Swagger

        :param image_url: The image_url of this Images.  # noqa: E501
        :type image_url: str
        :param small_image_url: The small_image_url of this Images.  # noqa: E501
        :type small_image_url: str
        """
        self.swagger_types = {
            'image_url': str,
            'small_image_url': str
        }

        self.attribute_map = {
            'image_url': 'image_url',
            'small_image_url': 'small_image_url'
        }
        self._image_url = image_url
        self._small_image_url = small_image_url

    @classmethod
    def from_dict(cls, dikt) -> 'Images':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Images of this Images.  # noqa: E501
        :rtype: Images
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image_url(self) -> str:
        """Gets the image_url of this Images.


        :return: The image_url of this Images.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url: str):
        """Sets the image_url of this Images.


        :param image_url: The image_url of this Images.
        :type image_url: str
        """

        self._image_url = image_url

    @property
    def small_image_url(self) -> str:
        """Gets the small_image_url of this Images.


        :return: The small_image_url of this Images.
        :rtype: str
        """
        return self._small_image_url

    @small_image_url.setter
    def small_image_url(self, small_image_url: str):
        """Sets the small_image_url of this Images.


        :param small_image_url: The small_image_url of this Images.
        :type small_image_url: str
        """

        self._small_image_url = small_image_url