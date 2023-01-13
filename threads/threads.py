import time
import random
import threading

from .ascii import rerender

class Monitor(threading.Thread):

    def __init__(self, threads, width=80, freq=25, delay=1):
        super(Monitor, self).__init__()
        self.threads = threads
        self.delay = delay
        self.running = True
        self.freq = freq
        self.width = width

    def toggle(self):
        self.running = not self.running

    def run(self):
        while self.running:
            rerender(self.view())
            time.sleep(1 / self.freq)

        time.sleep(self.delay)
        rerender(self.view())
        time.sleep(self.delay)
        print()
        print(self.bye())

    def bye(self):
        return f"quit in {self.delay}"

    def lfringe(self):
        return "[| "

    def rfringe(self):
        return " |]"

    def view(self):
        a = f"<monitor: {self.running}>"
        b = " | ".join(str((t.is_alive(), t.v)) for t in self.threads)
        len_a = len(a)
        len_b = min(len(b), 60)
        gap = self.width - len_b - len_a
        return self.lfringe() + b + (" " * gap) + a + self.rfringe()


class Dummy(threading.Thread):

    def __init__(self):
        super(Dummy, self).__init__()
        self.v = 0

    def run(self):
        for i in range(8):
            # print(self.getName())
            self.v = random.randint(1,10)
            time.sleep(0.5 + random.random())
