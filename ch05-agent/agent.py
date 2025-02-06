class Actor:
    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print(type(self).__name__, "is occupied with current movie")

    def available(self):
        self.is_busy = False
        print(type(self).__name__, "is free for the movie")

class Agent:
    def __init__(self):
        self.actor = None
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.is_busy:
            self.actor.occupied()
        else:
            self.actor.available()

if __name__ == '__main__':
    a = Agent()
    a.work()