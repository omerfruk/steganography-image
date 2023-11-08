#
# Bu kod, verilen bir görüntüye metni gizler ve sonucu kaydeder.
#

from PIL import Image

def MesajGizle(yollananGoruntu, msj):
    gizlenecekDegerler = ""

    byteDizisi = msj.encode('utf-8')  # Metni bir byte dizisine çevir

    gizlenecekDegerler += format(byteDizisi[0], '08b')  # 1. karakteri 8 bit olarak ekle
    gizlenecekDegerler += format(byteDizisi[1], '08b')  # 2. karakteri 8 bit olarak ekle
    gizlenecekDegerler += format(byteDizisi[2], '08b')  # 3. karakteri 8 bit olarak ekle

    gizlenenAdeti = 0
    for i in range(yollananGoruntu.width):
        for j in range(yollananGoruntu.height):
            R, G, B = yollananGoruntu.getpixel((i, j))

            gizlenecekBit_1 = gizlenecekDegerler[gizlenenAdeti] if gizlenenAdeti < len(gizlenecekDegerler) else ""
            gizlenecekBit_2 = gizlenecekDegerler[gizlenenAdeti + 1] if gizlenenAdeti + 1 < len(gizlenecekDegerler) else ""
            gizlenecekBit_3 = gizlenecekDegerler[gizlenenAdeti + 2] if gizlenenAdeti + 2 < len(gizlenecekDegerler) else ""

            binary_R = format(R, '08b')
            binary_G = format(G, '08b')
            binary_B = format(B, '08b')

            binary_R = binary_R[:-1] + gizlenecekBit_1
            binary_G = binary_G[:-1] + gizlenecekBit_2
            binary_B = binary_B[:-1] + gizlenecekBit_3

            R = int(binary_R, 2)
            G = int(binary_G, 2)
            B = int(binary_B, 2)

            yollananGoruntu.putpixel((i, j), (R, G, B))

            gizlenenAdeti += 3
            if gizlenenAdeti >= 24:  # 24 bit mesaj gizlendiğinde çık
                break
        if gizlenenAdeti >= 24:
            break

    yollananGoruntu.save('images/baboon_hide_message.png')

    return yollananGoruntu

# Görüntüyü yükle
image = Image.open('images/baboon.png')

# Mesaj gizleme işlemi
new_image = MesajGizle(image, "FAR")
