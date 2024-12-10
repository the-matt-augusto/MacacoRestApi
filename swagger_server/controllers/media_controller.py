import connexion
import six

from swagger_server.models.media import Media  # noqa: E501
from swagger_server.models.title import Title  # noqa: E501
from swagger_server import util


def create_media(body=None):  # noqa: E501
    """Place an order for a pet

    Place a new order in the store # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Media
    """
    if connexion.request.is_json:
        body = Media.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_media(id=None, title=None):  # noqa: E501
    """Place an order for a pet

    Place a new order in the store # noqa: E501

    :param id: 
    :type id: str
    :param title: 
    :type title: dict | bytes

    :rtype: Media
    """
    if connexion.request.is_json:
        title = Title.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_media():  # noqa: E501
    """Place an order for a pet

    Place a new order in the store # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_media():  # noqa: E501
    """Place an order for a pet

    Place a new order in the store # noqa: E501


    :rtype: Media
    """
    return 'do some magic!'


def update_media(body=None):  # noqa: E501
    """Place an order for a pet

    Place a new order in the store # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Media
    """
    if connexion.request.is_json:
        body = Media.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_media(id=None, title=None):  # noqa: E501
    """Place an order for a pet

    Place a new order in the store # noqa: E501

    :param id: 
    :type id: str
    :param title: 
    :type title: dict | bytes

    :rtype: Media
    """
    if connexion.request.is_json:
        title = Title.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
