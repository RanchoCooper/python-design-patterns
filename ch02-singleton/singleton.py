class Singleton(object):

    instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

if __name__ == '__main__':
    s = Singleton()
    s1 = Singleton()
    print(s is s1)  # True