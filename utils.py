from python_random_strings import random_strings
from models import Link


def generate_short_link():
    """
    It is responsible for creating random short links

    retrun : random string for short link
    """

    while True:
        random_flag = random_strings.random_letters(8)

        link_qury = Link.select().where(Link.short_link == random_flag)

        if link_qury.exists():
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
