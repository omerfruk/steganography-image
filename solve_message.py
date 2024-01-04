#
#  Bu kod, bir görüntüden gizlenmiş metni çıkarır ve çıkarılan mesajı döndürür.
#

from PIL import Image

def MesajCikar(yollananGoruntu):
    okunanBitler = ""
    okunamaAdeti = 0
    for i in range(yollananGoruntu.width):
        for j in range(yollananGoruntu.height):
            R, G, B = yollananGoruntu.getpixel((i, j))

            okunanBitler += format(R, '08b')[-1]
            okunanBitler += format(G, '08b')[-1]
            okunanBitler += format(B, '08b')[-1]

            okunamaAdeti += 3
            if okunamaAdeti >= 8 and okunanBitler[-8:] == "00000000":
                break
        if okunamaAdeti >= 8 and okunanBitler[-8:] == "00000000":
            break

    byteDizisi = [int(okunanBitler[i:i + 8], 2) for i in range(0, len(okunanBitler), 8)]
    okunanDegerler = bytes(byteDizisi).decode('utf-8').replace("\x00", "")

    return okunanDegerler

# Görüntüyü yükle
image = Image.open('images/baboon_hide_message.png')

# Mesaj çıkarma işlemi
mesaj = MesajCikar(image)

print("Çıkarılan Mesaj:", mesaj)
