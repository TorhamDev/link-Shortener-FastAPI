from python_random_strings import random_strings
from models.links import Link
from typing import Union
from tools.database import redis_obj as redis


def generate_short_link():
    """
    It is responsible for creating random short links

    return : random string for short link
    """

    while True:
        random_flag = random_strings.random_letters(8)

        link_query = Link.select().where(Link.short_link == random_flag)

        if link_query.exists():
            continue

        else:
            return random_flag


def create_short_link_record(link_address: str) -> str:
    """
    It is responsible for create a new database record for new short link

    params : link_address : user input link

    return : random short link str
    """

    random_link = generate_short_link()

    short_link = Link(address=link_address, short_link=random_link)
    short_link.save()

    return random_link


def check_link_is_exists(link) -> Union[str, bool]:
    """
    It is responsible for checking input link already exists or not

    params : link : user input link for generating short link

    return : short link if exists or False
    """

    query = Link.select().where(Link.address == link)
    if query.exists():
        return query[0].short_link
    else:
        return False


def set_cache(key: str, value: str, expire_time=None) -> bool:
    """
    Set cache in redis with expire time

    params : key : key for set data in redis
    params : value : data want to save in redis as cache
    params : expire_tim : expire time for cache, also can be null. that is mean forever :)

    return: True or False
    """

    redis.set(key, value)
    if expire_time is not None:
        redis.expire(key, expire_time)

    return True
