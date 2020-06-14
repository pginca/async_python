import json
import requests


def sync_request(id):
    session = requests.Session()
    print(f'Start request with id {id}')
    session.get(f'https://jsonplaceholder.typicode.com/todos/{id}')
    print(f'Done request with id {id}')