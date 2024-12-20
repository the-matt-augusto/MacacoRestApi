# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.title import Title  # noqa: F401,E501
from swagger_server import util


class Media(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, title: Title=None):  # noqa: E501
        """Media - a model defined in Swagger

        :param id: The id of this Media.  # noqa: E501
        :type id: str
        :param title: The title of this Media.  # noqa: E501
        :type title: Title
        """
        self.swagger_types = {
            'id': str,
            'title': Title
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title'
        }
        self._id = id
        self._title = title

    @classmethod
    def from_dict(cls, dikt) -> 'Media':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Media of this Media.  # noqa: E501
        :rtype: Media
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Media.


        :return: The id of this Media.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Media.


        :param id: The id of this Media.
        :type id: str
        """

        self._id = id

    @property
    def title(self) -> Title:
        """Gets the title of this Media.


        :return: The title of this Media.
        :rtype: Title
        """
        return self._title

    @title.setter
    def title(self, title: Title):
        """Sets the title of this Media.


        :param title: The title of this Media.
        :type title: Title
        """

        self._title = title
