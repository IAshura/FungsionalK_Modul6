# TODO 0 : Import beberapa library lain yang dibutuhkan
from cgitb import text
from PIL import Image, ImageDraw, ImageFont

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open('direktory/argus-light-of-dawn-skin-mobile-legends-uhdpaper.com-4K-6.2869.jpg')
overlay_image = Image.open('direktory/908481.512.webp')

# TODO 2 : Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert('RGBA')

# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center), overlay_image)

# TODO 5 : Simpan gambar hasil edit
background_image.save('hasil_edit_2.jpg')

# TODO 6 : Tampilkan
background_image.show()