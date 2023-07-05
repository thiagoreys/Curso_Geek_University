from utils.helper import date_para_str, str_para_date
from datetime import date

class Cliente:
    c = 101

    def __init__(self, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo = Cliente.c
        self.__nome = nome.title()
        self.__email = email.lower()
        self.__cpf = cpf
        self.__data_nascimento = str_para_date(data_nascimento)
        self.__data_cadastro = date.today()
        Cliente.c += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def data_nascimento(self) -> str:
        return date_para_str(self.__data_nascimento)
    
    @property
    def data_cadastro(self) -> str:
        return date_para_str(self.__data_cadastro)
        
    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nData Nascimento: {self.data_nascimento} \nData Cadastro: {self.data_cadastro}'