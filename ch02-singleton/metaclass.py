class MyInt(type):
    def __call__(cls, *args, **kwds):
        print("***** Here's My int *****", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwds)

class Int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("int object with values (%d, %d) created!" % (x, y))


if __name__ == '__main__':
    i = Int(4, 5)