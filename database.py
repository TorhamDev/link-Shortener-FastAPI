from contextvars import ContextVar
import redis
import peewee


redis_obj = redis.Redis(host="localhost", port=6379, db=0)

DATABASE_NAME = "app.db"
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


db = peewee.MySQLDatabase('shortener_link', user='root', password='mysql', host='localhost', port=3306)
db._state = PeeweeConnectionState()
