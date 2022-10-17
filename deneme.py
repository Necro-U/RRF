import threading
from time import sleep


class deneme:
    __slots__ = ["x", "b"]

    def __init__(self) -> None:
        self.x = 5

    def func(self):
        print("sea")
        sleep(1)
        print("ase")

    def run(self):
        func = threading.Thread(target=self.func)
        func.start()


a = deneme()

a.b = 7

print(a.b)
