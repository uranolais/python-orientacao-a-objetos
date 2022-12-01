#Atividade 01
class Conta:

    def __init__(self, numero, saldo, limite ):
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite
        self.__tarifaTransferencia = 8.0


    def saca(self,valor):

        if valor < (self.__saldo + self.__limite):
                self.__saldo -= valor
                print("Saque efetuado.")
        else:
                print("Saldo insuficiente.")



    def transfere(self, valor, destino):


            valorTotal = valor + self.__tarifaTransferencia

           if valorTotal < (self.__saldo + self.__limite):

                self.__saldo -= valorTotal
                destino.deposita(valor)

                print("Transferência efetuada.")
            else:
                print("Saldo insuficiente.")


    # outros métodos omitidos...
