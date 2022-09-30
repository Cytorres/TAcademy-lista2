from src.application.aluno import Aluno

def mensagem(aluno_objeto: Aluno) -> None:
    print(aluno_objeto.__dict__)
