from python_random_strings import random_strings
from models import Link
from peewee import Model

def generate_short_link(link_address: str):

    while True:
        random_flag = random_strings.random_letters(8)
        
        link_qury = Link.select().where(Link.short_link == random_flag)
        
        if link_qury.exists():
            continue
        
        else:
            return random_flag