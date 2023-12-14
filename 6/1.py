# TODO 0: Import library lain yang dibutuhkan
from PIL import ImageDraw, ImageFont
from PIL import Image

# TODO 1: Lakukan load image pada variabel berikut
gambarku = Image.open('direktory/argus-light-of-dawn-skin-mobile-legends-uhdpaper.com-4K-6.2869.jpg')

# TODO 2: Ubah gambar menjadi hitam-putih
gambarBW = gambarku.convert('L')

# TODO 3: Tambahkan text dengan font Arial dan ukuran 24 sesuai kriteria
draw = ImageDraw.Draw(gambarBW)
font_path = 'font/Roboto,Whisper/Roboto/Roboto-BoldItalic.ttf'
font = ImageFont.truetype(font_path, 60)
text = "Muhammad Mazen Fayiz Birizqie \n 202110370311513"

# Menghitung ukuran teks menggunakan bounding box
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

text_x = (gambarBW.width - text_width) // 2
text_y = (gambarBW.height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
imagenew = 'hasil_edit_1.jpg'
gambarBW.save(imagenew)

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()