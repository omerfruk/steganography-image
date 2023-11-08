import cv2
import numpy as np

def RenkDegistir8Bit(yollananGoruntu, yeniRenk):
    height, width = yollananGoruntu.shape[:2]  # Görüntü boyutunu al

    # Yeni bir 8-bitlik gri seviye görüntü oluşturun
    bmp = np.zeros((height, width), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            renk = yollananGoruntu[y, x]
            R, G, B = renk[2], renk[1], renk[0]

            yeniDeger = R + 50  # 0-255
            if yeniDeger > 255:
                yeniDeger = 255
            if yeniDeger < 0:
                yeniDeger = 0

            bmp[y, x] = yeniDeger

    return bmp

# Görüntüyü yükle
image = cv2.imread('images/baboon.png')

# Renk değiştirme işlemi
new_image = RenkDegistir8Bit(image, yeniRenk=100)

# Sonucu kaydet
cv2.imwrite('images/baboon_change_color8_bit.png', new_image)