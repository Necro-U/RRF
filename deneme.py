import threading
from time import sleep


class deneme:
    def func(self):
        print("sea")
        sleep(1)
        print("ase")

    def run(self):
        func = threading.Thread(target=self.func)
        func.start()


a = deneme()

a.run()
