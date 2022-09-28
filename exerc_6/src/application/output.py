from src.application.domain import Aluno


def mensagem(aluno_objeto:Aluno) -> None:
    print(aluno_objeto.nome)
    print(aluno_objeto.classe)
    print(aluno_objeto.idade)