from mod.estado import Estado

class EstadoContagem(Estado):
	
	'''
	Construtor da classe EstadoContagem

	@param valor
	'''
	def __init__(self,valor):
		self.__valor=valor
		self.__id_valor = hash(self.__valor)


	def id_valor(self):
		
		return self.__id_valor

	@property
	def valor(self):
		return self.__valor
		
