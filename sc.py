#
# Bu Python kodu, iki görüntü arasındaki benzerlik katsayısını hesaplar.
#
from PIL import Image

def SC(b1, b2):
    sum1 = 0
    sum2 = 0

    for i in range(b1.width):
        for j in range(b1.height):
            p1 = b1.getpixel((i, j))
            p2 = b2.getpixel((i, j))
            sum1 += p1[0] ** 2  # Kırmızı kanal
            sum2 += p2[0] ** 2  # Kırmızı kanal
            # sum1 += p1[1] ** 2  # Yeşil kanal
            # sum2 += p2[1] ** 2  # Yeşil kanal
            # sum1 += p1[2] ** 2  # Mavi kanal
            # sum2 += p2[2] ** 2  # Mavi kanal

    if sum2 == 0:
        return 0

    similarity = sum1 / sum2

    return round(similarity, 2)

# Görüntüleri yükleyin (b1 ve b2)
image1 = Image.open('images/baboon.png')
image2 = Image.open('images/baboon_hide_message.png')

# Benzerlik katsayısını hesaplayın
similarity = SC(image1, image2)

print("Benzerlik Katsayısı:", similarity)