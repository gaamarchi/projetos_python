import random
class simulador_de_dados():
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.mensagem = "deseja gerar um novo valor de dado "
        

    def  iniciar(self):
        while True:
            resposta = self.Pergunta()
            if(resposta=="sim")or(resposta =="s"):
                self.gerarValorDoDado()
            elif(resposta=="nao") or (resposta=="n"):
                print("nos agradecemos sua participação")
                break
            else:
                print('digte sim ou não')


    def gerarValorDoDado(self):
        print(random.randint(self.valorMinimo,self.valorMaximo))

    def Pergunta(self):
        return input(self.mensagem).lower()
 

simulador = simulador_de_dados()
simulador.iniciar()