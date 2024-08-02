# personagem : classe mae
# heroi: controlado pelo usuario
# inimigo: adversarop do usuario

import random

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} \nVida: {self.get_vida()} \nNível: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0    
    
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 6, self.get_nivel() * 10)
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"
    
    
'''teste1 = Heroi(nome="Batman", vida="100", nivel="5", habilidade="Rico")

print(teste1.exibir_detalhes())

teste2 = Inimigo(nome="Coringa", vida="50", nivel="6", tipo="Maluco")

print(teste2.exibir_detalhes())'''

class Jogo:
    '''Classe orquestradora do jogo'''

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Batman", vida=100, nivel=5, habilidade="Rico")
        self.inimigo = Inimigo(nome="Coringa", vida=50, nivel=6, tipo="Maluco")

    def iniciar_batalha(self):
        '''Fazer gestão da batalha em turnos'''
        print("Iniciando Batalha")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens: ")
            print(f"\n{self.heroi.exibir_detalhes()}")
            print(f"\n{self.inimigo.exibir_detalhes()}")

            input("\nPressione enter para atacar ...")
            escolha = input("Escolha (1- Ataque Normal, 2- Ataque Especial): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida, escolha novamente!")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\nParabéns, você venceu")
        else:
            print(f"\nYou lose")


#Criar instancia do jogo e iniciar a batalha

jogo = Jogo()
jogo.iniciar_batalha()