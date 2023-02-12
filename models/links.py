import peewee

from tools.database import db


class Link(peewee.Model):
    address = peewee.CharField(index=True)
    short_link = peewee.CharField(index=True, max_length=8)

    class Meta:
        database = db


db.connect()
db.create_tables([Link], safe=True)
db.close()
