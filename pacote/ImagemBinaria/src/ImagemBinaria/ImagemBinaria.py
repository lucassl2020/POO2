import cv2 as cv
import numpy as np


class ImagemBinaria():
	"""

	Abrindo imagem e transformando em binaria.
	
	:ivar self._imagem_binaria: Usado para armazenar a imagem binaria
	:vartype self._clientes: list

	"""
	def __init__(self, path):
		img = cv.imread(path, cv.IMREAD_GRAYSCALE)

		img = img.astype('float32') / 255

		img[img > 0.5] = 1
		img[img <= 0.5] = 0

		self._imagem_binaria = np.uint8(img)

	@property
	def imagem_binaria(self):
		return self._imagem_binaria

	@imagem_binaria.setter
	def imagem_binaria(self, img):
		self._imagem_binaria = img

	@property
	def shape(self):
		return self.imagem_binaria.shape

	@property
	def size(self):
		return self.imagem_binaria.size

	def rotacao(self, graus, atualizar_imagem=False):
		"""

		Rotaciona a imagem em N graus sentido anti-horario.
			
		:param graus: Quantidade de graus em que a imagem sera rotacionada.
		:type graus: int
		:param atualizar_imagem: Se True, salva as modificações feitas na imagem.
		:type atualizar_imagem: bool

		:return: Imagem binaria rotacionada
		:rtype: lista
		"""
		centro = (self.shape[1] / 2, self.shape[0] / 2) 

		matriz_de_rotacao = cv.getRotationMatrix2D(centro, graus, 1.0)

		img_rotacao = cv.warpAffine(self.imagem_binaria, matriz_de_rotacao, (self.shape[1], self.shape[0]))

		if atualizar_imagem:
			self.imagem_binaria = img_rotacao

		return img_rotacao

	def translacao(self, x, y, atualizar_imagem=False):
		"""

		Desloca a imagem nos eixos x e y.
			
		:param x: Se positivo desloca N pixels para direita, se negativo desloca para esquerda.
		:type x: int
		:param y: Se positivo desloca N pixels para baixo, se negativo desloca para cima.
		:type y: int

		:return: Imagem binaria deslocada
		:rtype: lista
		"""
		deslocamento = np.float32([[1, 0, x], [0, 1, y]])
		
		img_translacao = cv.warpAffine(self.imagem_binaria, deslocamento, (self.shape[1], self.shape[0]))

		if atualizar_imagem:
			self.imagem_binaria = img_translacao

		return img_translacao

	def dilatacao(self, kernel_shape, atualizar_imagem=False):
		"""

		Aplica dilatação na imagem.
			
		:param kernel_shape: Dimensão do kernel. 
		:type kernel_shape: int

		:return: Imagem binaria dilatada.
		:rtype: lista
		"""
		kernel = np.ones(kernel_shape, np.uint8) 

		img_dilatacao = cv.dilate(self.imagem_binaria, kernel, iterations = 1)

		if atualizar_imagem:
			self.imagem_binaria = img_dilatacao

		return img_dilatacao

	def erosao(self, kernel_shape, atualizar_imagem=False):
		"""

		Aplica erosão na imagem.
			
		:param kernel_shape: Dimensão do kernel. 
		:type kernel_shape: int

		:return: Imagem binaria erodida.
		:rtype: lista
		"""
		kernel = np.ones(kernel_shape, np.uint8) 

		img_erosao = cv.erode(self.imagem_binaria, kernel, iterations = 1) 

		if atualizar_imagem:
			self.imagem_binaria = img_erosao

		return img_erosao

	def abertura(self, kernel_shape, atualizar_imagem=False):
		"""

		Aplica erosão e logo após, dilatação na imagem.
			
		:param kernel_shape: Dimensão do kernel. 
		:type kernel_shape: int

		:return: Imagem binaria com abertura aplicada.
		:rtype: lista
		"""
		kernel = np.ones(kernel_shape, np.uint8) 

		img_abertura = cv.morphologyEx(self.imagem_binaria, cv.MORPH_OPEN, kernel)

		if atualizar_imagem:
			self.imagem_binaria = img_abertura

		return img_abertura

	def fechamento(self, kernel_shape, atualizar_imagem=False):
		"""

		Aplica dilatação e logo após, erosão na imagem.
			
		:param kernel_shape: Dimensão do kernel. 
		:type kernel_shape: int

		:return: Imagem binaria com fechamento aplicado.
		:rtype: lista
		"""
		kernel = np.ones(kernel_shape, np.uint8)

		img_fechamento = cv.morphologyEx(self.imagem_binaria, cv.MORPH_CLOSE, kernel)

		if atualizar_imagem:
			self.imagem_binaria = img_fechamento

		return img_fechamento

	def componentes_conectados(self):
		"""

		Identifica pixels que pertencem ao mesmo objeto.

		:return: Imagem binaria com os objetos classificados.
		:rtype: lista
		"""
		_, objetos = cv.connectedComponents(self.imagem_binaria)

		return objetos

	def mostrar(self):
		img = self.imagem_binaria * 255

		cv.imshow("imagem binaria", img) 

		cv.waitKey(0)

		cv.destroyAllWindows()

	def salvar(self, path):
		img = self.imagem_binaria * 255

		cv.imwrite(path, img)

	def __str__(self):
		return self.imagem_binaria.__str__()


def dice(img1, img2, smooth=1):
	if len(img1.imagem_binaria) == len(img2.imagem_binaria):
		img1 = img1.imagem_binaria.flatten()
		img2 = img2.imagem_binaria.flatten()

		intersecao = img1 * img2

		return ((2 * intersecao.sum()) + smooth)/((img1.sum() + img2.sum()) + smooth)
	return None

def iou(img1, img2, smooth=1):
	if len(img1.imagem_binaria) == len(img2.imagem_binaria):
		img1 = img1.imagem_binaria.flatten()
		img2 = img2.imagem_binaria.flatten()

		intersecao = img1 * img2

		return (intersecao.sum() + smooth)/((img1.sum() + img2.sum() - intersecao.sum()) + smooth)
	return None

def acuracia(img1, img2):
    if len(img1.imagem_binaria) == len(img2.imagem_binaria):
        result = img1.imagem_binaria == img2.imagem_binaria
        
        return len(result[result == True]) / len(img1.imagem_binaria.flatten())
    return None