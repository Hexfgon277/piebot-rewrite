import json


def get_data(location):
    with open(f'config/{location}.json', encoding='utf-8') as f:
        return json.load(f)


class Config:
    core = get_data('core')