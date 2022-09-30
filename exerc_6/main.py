from src.application.aluno import Aluno
from src.application.input import abre_arquivo_json
from src.application.output import mensagem

if __name__ == '__main__':
    dict_data = abre_arquivo_json()
    aluno = Aluno(**dict_data)
    mensagem(aluno)
