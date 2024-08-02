

# classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f'Meu nome é {self.nome} e eu tenho {self.idade} anos'


#objeto
pessoa1 = Pessoa("Bruno Martinez", 67)
pessoa2 = Pessoa(nome="Kleber", idade=58)

#print(pessoa1)

print(f'Nome: {pessoa1.nome}')
print(f'Idade: {pessoa1.idade}')

mensagem = pessoa1.saudacao()

print(mensagem)

#print(pessoa2)

print(f'Nome: {pessoa2.nome}')
print(f'Idade: {pessoa2.idade}')

mensagem = pessoa2.saudacao()

print(mensagem)