import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

# Fungsi Translasi
def Translasi(image, shiftX, shiftY):
    # Geser piksel pada sumbu Y
    imgTranslasi = np.roll(image, shift=shiftY, axis=0)
    # Geser piksel pada sumbu X
    imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1)
    
    # Hapus artefak akibat pergeseran
    if shiftY > 0:
        imgTranslasi[:shiftY, :] = 0  # Baris atas
    elif shiftY < 0:
        imgTranslasi[shiftY:, :] = 0  # Baris bawah
    if shiftX > 0:
        imgTranslasi[:, :shiftX] = 0  # Kolom kiri
    elif shiftX < 0:
        imgTranslasi[:, shiftX:] = 0  # Kolom kanan

    return imgTranslasi

# Baca Gambar
image = img.imread(r"D:\Kampus\SEMESTER 5\Pengolahan Citra Digital\Sesi 5 & 6\Horse.jpg")

# Panggil Fungsi Translasi
imgResult = Translasi(image, shiftX=50, shiftY=300)

# Tampilkan Gambar
plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis("off")

plt.subplot(2, 1, 2)
plt.title("Translated Image")
plt.imshow(imgResult)
plt.axis("off")

plt.show()
