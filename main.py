# toda classe tem atributos (caracteristicas)
# e metodos (acoes)

#atributo: preto com 10cm de altura, com os metodos, mudar canal, aumentar volume
class ControleRemoto:
	def __init__(self, cor, altura, profundidade, largura):
		self.cor = cor
		self.altura = altura
		self.profundida = profundidade
		self.largura = largura

	def passar_canal(self, botao):
		if botao == "+":
			print("Aumentar o Canal")
		if botao == "-":
			print("Diminuir o Canal")



controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
print(controle_remoto.cor, controle_remoto.altura)
controle_remoto.passar_canal("+")


controle_remoto_2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")
print(controle_remoto_2.cor)