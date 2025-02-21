from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, receive):
        self.recv = receive

    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receive):
        self.recv = receive
        super().__init__(receive)

    def execute(self):
        self.recv.action()

class Receiver:
    def action(self):
        print("Receiver Action")

class Invoker:
    def __init__(self):
        self.cmd = None

    def command(self, command):
        self.cmd = command

    def execute(self):
        self.cmd.execute()

if __name__ == '__main__':
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()