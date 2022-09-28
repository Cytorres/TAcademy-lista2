import json

class Aluno():
    def __init__(self, nome:str, classe:str, idade:int) -> None:
        self.nome = nome
        self.classe = classe
        self.idade = idade

def abre_arquivo_json()-> Aluno:
    with open('src/application/aluno.json' , 'r') as aluno:
        aluno_dict = json.load(aluno)
        aluno_objeto = Aluno(**aluno_dict)

    return aluno_objeto
