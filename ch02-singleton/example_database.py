import sqlite3

class MetaSingleton(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Database(metaclass=MetaSingleton):

    connection = None

    def __init__(self):
        self.cursor_obj = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db.sqlite3')
            self.cursor_obj = self.connection.cursor()
        return self.cursor_obj


if __name__ == '__main__':
    db1 = Database().connect()
    db2 = Database().connect()
    print(db1.connection is db2.connection)

