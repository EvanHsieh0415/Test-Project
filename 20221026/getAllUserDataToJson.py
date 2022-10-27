from json import load, dump
from typing import Generator
from discord import User

def get_all_user_data(user_list: list[User]) -> Generator[list]:
    head = [*User.__dict__]
    for user in user_list:
        yield [*user.__dict__.values()]

def save_data(data: Generator[list], path: str='./output', extension: str='.json', **open_options):
    with open(f'{path}{extension}', 'w', **open_options) as file:
        file.write('[\n')
        for item in data:
            file.write(f'  {item},\n')
        file.write(']')