import json


def abre_arquivo_json() -> dict:
    with open('src/application/aluno.json', 'r') as json_data:
        return json.load(json_data)
