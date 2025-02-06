class SingletonLazy(object):

    __instance = None

    def __init__(self):
        if not SingletonLazy.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = SingletonLazy()
        return cls.__instance

if __name__ == '__main__':
    s = SingletonLazy()
    print("Object created", SingletonLazy.getInstance())
    s1 = SingletonLazy()
    print("Object created", SingletonLazy.getInstance())
    # FIXME output is False
    print(s is s1)  # True