import json

with open('zh_tw.json', encoding='utf8') as file:
    data = json.load(file)

for k, v in data.items():
    print(f'{k}: {v}')