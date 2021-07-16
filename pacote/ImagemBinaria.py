import cv2 as cv
import numpy as np


class ImagemBinaria():
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
		centro = (self.shape[1] / 2, self.shape[0] / 2) 

		matriz_de_rotacao = cv.getRotationMatrix2D(centro, graus, 1.0)

		img_rotacao = cv.warpAffine(self.imagem_binaria, matriz_de_rotacao, (self.shape[1], self.shape[0]))

		if atualizar_imagem:
			self.imagem_binaria = img_rotacao

		return img_rotacao

	def translacao(self, x, y, atualizar_imagem=False):
		deslocamento = np.float32([[1, 0, x], [0, 1, y]])
		
		img_translacao = cv.warpAffine(self.imagem_binaria, deslocamento, (self.shape[1], self.shape[0]))

		if atualizar_imagem:
			self.imagem_binaria = img_translacao

		return img_translacao

	def dilatacao(self, kernel_shape, atualizar_imagem=False):
		kernel = np.ones(kernel_shape, np.uint8) 

		img_dilatacao = cv.dilate(self.imagem_binaria, kernel, iterations = 1)

		if atualizar_imagem:
			self.imagem_binaria = img_dilatacao

		return img_dilatacao

	def erosao(self, kernel_shape, atualizar_imagem=False):
		kernel = np.ones(kernel_shape, np.uint8) 

		img_erosao = cv.erode(self.imagem_binaria, kernel, iterations = 1) 

		if atualizar_imagem:
			self.imagem_binaria = img_erosao

		return img_erosao

	def abertura(self, kernel_shape, atualizar_imagem=False):
		kernel = np.ones(kernel_shape, np.uint8) 

		img_abertura = cv.morphologyEx(self.imagem_binaria, cv.MORPH_OPEN, kernel)

		if atualizar_imagem:
			self.imagem_binaria = img_abertura

		return img_abertura

	def fechamento(self, kernel_shape, atualizar_imagem=False):
		kernel = np.ones(kernel_shape, np.uint8)

		img_fechamento = cv.morphologyEx(self.imagem_binaria, cv.MORPH_CLOSE, kernel)

		if atualizar_imagem:
			self.imagem_binaria = img_fechamento

		return img_fechamento

	def componentes_conectados(self):
		_, objetos = cv.connectedComponents(self.imagem_binaria)

		return objetos

	def mostrar(self):
		img = self.imagem_binaria * 255

		cv.imshow("imagem binaria", img) 

		cv.waitKey(0)

		cv.destroyAllWindows()

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