import cv2
import numpy as np

valr_filtro = 353
# Carrega a imagem
image = cv2.imread("C:/Users/lmmot/Documents/trabalho/mi1.jpg")

# Aplica o Filtro Gaussiano para suavização
blurred = cv2.GaussianBlur(image, (valr_filtro, valr_filtro), 0)

# Subtrai a imagem suavizada da imagem original para obter a máscara de nitidez
unsharp_mask = cv2.subtract(image, blurred)

# Adiciona a máscara de nitidez à imagem original para obter a imagem realçada
sharpened_image = cv2.add(image, unsharp_mask)

# Exibe as imagens original e realçada
cv2.imshow("Original", image)
cv2.imshow("Realçada", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
