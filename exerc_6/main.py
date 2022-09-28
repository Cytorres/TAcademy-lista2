from src.application.domain import  abre_arquivo_json
from src.application.output import mensagem

if __name__ == '__main__':
    aluno_json = abre_arquivo_json()
    mensagem(aluno_json)
 
 