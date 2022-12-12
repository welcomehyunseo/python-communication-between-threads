import random
import time

from queue import Queue
from threading import Thread


def sender(out_q: Queue):
    while True:
        num = random.randint(1, 10)
        out_q.put(num)
        print("sender")
        print(f'\tnum={num}')
        time.sleep(1)


def receiver(in_q: Queue):
    while True:
        num = in_q.get()
        print("receiver")
        print(f'\tnum={num}')


def main():
    q = Queue()
    t_0 = Thread(target=sender, args=(q,))
    t_0.start()
    t_1 = Thread(target=receiver, args=(q,))
    t_1.start()


if __name__ == '__main__':
    main()
