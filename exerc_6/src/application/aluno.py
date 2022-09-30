from dataclasses import dataclass


@dataclass
class Aluno():
    def __init__(self, nome: str, classe: str, idade: int) -> None:
        self.nome = nome
        self.classe = classe
        self.idade = idade
