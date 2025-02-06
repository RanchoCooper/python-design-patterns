class MetaSingleton(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Logger(metaclass=MetaSingleton):
    pass


if __name__ == '__main__':
    logger1 = Logger()
    logger2 = Logger()
    print(logger1 is logger2)