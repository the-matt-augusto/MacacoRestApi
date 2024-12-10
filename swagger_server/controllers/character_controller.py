import connexion
import six

from swagger_server.models.character import Character  # noqa: E501
from swagger_server.models.images import Images  # noqa: E501
from swagger_server import util


def create_character(body):  # noqa: E501
    """Add a new pet to the store

    Add a new pet to the store # noqa: E501

    :param body: Create a new pet in the store
    :type body: dict | bytes

    :rtype: Character
    """
    if connexion.request.is_json:
        body = Character.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_character(id, name, name_kanji, nicknames, rarity, gender, images, media_id):  # noqa: E501
    """Add a new pet to the store

    Add a new pet to the store # noqa: E501

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param name_kanji: 
    :type name_kanji: str
    :param nicknames: 
    :type nicknames: List[str]
    :param rarity: 
    :type rarity: int
    :param gender: 
    :type gender: str
    :param images: 
    :type images: dict | bytes
    :param media_id: 
    :type media_id: List[str]

    :rtype: Character
    """
    if connexion.request.is_json:
        images = Images.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_character(pet_id):  # noqa: E501
    """Deletes a pet

    delete a pet # noqa: E501

    :param pet_id: Pet id to delete
    :type pet_id: int

    :rtype: None
    """
    return 'do some magic!'


def read_character(status=None):  # noqa: E501
    """List characters by filter

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: str

    :rtype: List[Character]
    """
    return 'do some magic!'


def update_character(body):  # noqa: E501
    """Update an existing character

    Update an existing character by Id # noqa: E501

    :param body: Update an existent pet in the store
    :type body: dict | bytes

    :rtype: Character
    """
    if connexion.request.is_json:
        body = Character.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_character(id, name, name_kanji, nicknames, rarity, gender, images, media_id):  # noqa: E501
    """Update an existing character

    Update an existing character by Id # noqa: E501

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param name_kanji: 
    :type name_kanji: str
    :param nicknames: 
    :type nicknames: List[str]
    :param rarity: 
    :type rarity: int
    :param gender: 
    :type gender: str
    :param images: 
    :type images: dict | bytes
    :param media_id: 
    :type media_id: List[str]

    :rtype: Character
    """
    if connexion.request.is_json:
        images = Images.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
