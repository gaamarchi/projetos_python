import random
class simulador_de_dados():
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo =6
        self.mensagem = "deseja gerar um novo valor de dado "

    def  iniciar(self):
        try:
            resposta = input(self.mensagem).lower()
            if(resposta=="sim")or(resposta =="s"):
                self.gerarValorDoDado()
            elif(resposta=="nao") or (resposta=="n"):
                print("nos agradecemos sua participação")
        except:
            print("por favor digite sim ou nao")
            self.iniciar()

            
    def gerarValorDoDado(self):
        print(random.randint(self.valorMinimo,self.valorMaximo))

simulador = simulador_de_dados()
simulador.iniciar()