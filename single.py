from time import time

from sync_request import sync_request


def main():
    ts = time()

    for id in range(1, 101):
        sync_request(id)

    print(f'Took {time() - ts} seconds')

if __name__ == '__main__':
    main()