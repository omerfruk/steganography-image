#
# Her pikseli işler ve her pikselin R, G ve B bileşenlerinin ortalamasını alarak gri tonlama işlemi yapar.
#

from PIL import Image

def GriTonaDonustur(yollananGoruntu):
    width, height = yollananGoruntu.size

    for i in range(width):
        for j in range(height):
            pixel = yollananGoruntu.getpixel((i, j))
            R, G, B = pixel[0], pixel[1], pixel[2]

            ort = (R + G + B) // 3

            yollananGoruntu.putpixel((i, j), (ort, ort, ort))

    return yollananGoruntu

image = Image.open('images/baboon.png')

# Renk değiştirme işlemi
new_image = GriTonaDonustur(image)

# Sonucu kaydet
new_image.save('images/baboon_frost_gray_tone.png')