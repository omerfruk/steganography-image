#
# Bu Python kodu, iki görüntü arasındaki PSNR (Peak Signal-to-Noise Ratio) değerini hesaplar.
#
from PIL import Image
import math

def PSNRValue(b1, b2):
    sum_squared_diff = 0

    for i in range(b1.width):
        for j in range(b1.height):
            p1 = b1.getpixel((i, j))
            p2 = b2.getpixel((i, j))
            sum_squared_diff += (abs(p1[0] - p2[0]) ** 2)  # Kırmızı kanal
            # sum_squared_diff += (abs(p1[1] - p2[1]) ** 2)  # Yeşil kanal
            # sum_squared_diff += (abs(p1[2] - p2[2]) ** 2)  # Mavi kanal

    if sum_squared_diff == 0:
        sum_squared_diff = 1

    mse = sum_squared_diff / (b1.width * b1.height)
    psnr = 10 * math.log10((255 ** 2) / mse)

    return round(psnr, 2)

# Görüntüleri yükleyin (b1 ve b2)
image1 = Image.open('images/baboon.png')
image2 = Image.open('images/baboon_hide_message.png')

# PSNR değerini hesaplayın
psnr = PSNRValue(image1, image2)

print("PSNR Değeri:", psnr)
