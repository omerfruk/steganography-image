#
# Bu kod parçası, verilen bir görüntü dosyasını yükler, renk değişikliği yapar ve sonucu kaydeder.
# Her pikseli kontrol eder ve eğer belirli bir koşulu karşılıyorsa (R, G ve B değerleri 200'den büyükse), renk değişikliği yapar.
#
from PIL import Image
def RenkDegistir(yollananGoruntu,renkR=255, renkG=0, renkB=0):
    width, height = yollananGoruntu.size

    for i in range(width):
        for j in range(height):
            pixel = yollananGoruntu.getpixel((i, j))
            R, G, B = pixel[0], pixel[1], pixel[2]
            if R > 200 and G > 200 and B > 200:
                yollananGoruntu.putpixel((i, j), (renkR, renkG, renkB))

    return yollananGoruntu


# Görüntüyü yükle
image = Image.open('images/baboon.png')

# Renk değiştirme işlemi
new_image = RenkDegistir(image, renkR=100, renkG=200, renkB=50)

# Sonucu kaydet
new_image.save('images/baboon_change_color.png')