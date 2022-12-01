#Atividade 01
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibe_nome_e_sobrenome(self):
        print("{0} {1}".format(self.nome, self.sobrenome))


pessoa = Pessoa("Chalita", "Steppat")
pessoa.exibe_nome_e_sobrenome()

#Atividade 02
class Jogo:
    
    def __init__(self):
        self.contador = 0

    def incrementa(self):
        self.contador+=1

jogo = Jogo()
jogo.incrementa()
print(jogo.contador)

#Atividade 03
class Data:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatada(self):
        print("{0}/{1}/{2}".format(self.dia,self.mes,self.ano))
