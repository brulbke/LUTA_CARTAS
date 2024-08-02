# @classmethod
# @sataticmethod

class MinhaClasse:
    valor = 10 # atriuto da classe
    def __init__(self, nome) -> None:
        self.nome = nome #atributo da instancia

    #requer uma instancia para ser chamado
    def metodo_instancia(self):
        return f'Método da instancia chamado para {self.nome}'
    
    def metodo_instancia1(self):
        return f'Método da instancia chamado para {self.valor}'

    @classmethod
    def metodo_classe(cls):
        return f"Método da classe chamado para o valor = {cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return f"Metodo estático"
    
obj = MinhaClasse(nome= "Classe exemplo")

print(obj.metodo_instancia())

print(MinhaClasse.valor)

print(MinhaClasse.metodo_classe())

print(MinhaClasse.metodo_estatico())


    
    
class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca,modelo,ano)
    
configuracao1 = "Toyota, Corolla, 2024"

carro1 = Carro.criar_carro(configuracao1)

print(f"Marca: {carro1.marca} \nModelo: {carro1.modelo}\nAno: {carro1.ano} ")

class Matematica:

    @staticmethod
    def somar(a, b):
        return a + b
    
print(Matematica.somar(a=10, b=15))