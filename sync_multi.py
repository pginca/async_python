from time import time
from threading import Thread
from queue import Queue

from sync_request import sync_request


queue = Queue()

def worker():
    while True:
        id = queue.get()
        try:
            sync_request(id)
        finally:
            queue.task_done()

def main():
    ts = time()

    for _ in range(4):
        Thread(target=worker, daemon=True).start()
    
    for id in range(1, 101):
        queue.put(id)

    queue.join()
    print(f'Took {time() - ts} seconds')

if __name__ == '__main__':
    main()