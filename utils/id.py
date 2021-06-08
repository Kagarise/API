import random


def create_id(length):
    option = '01234567890abcdefghijklmnopqrstuvwxyz'
    id = ''
    for idx in range(length):
        id += random.choice(option)
    return id
