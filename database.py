from contextvars import ContextVar
from constants import (
    REDIS_DB,
    REDIS_DB_HOST,
    REDIS_DB_PORT,
    DB_HOST,
    DB_NAME,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
)
import peewee
import redis

redis_obj = redis.Redis(host=REDIS_DB_HOST, port=REDIS_DB_PORT, db=REDIS_DB)

db_state_default = {
    "closed": None,
    "conn": None,
    "ctx": None,
    "transactions": None,
}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.MySQLDatabase(
    DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
)
db._state = PeeweeConnectionState()
