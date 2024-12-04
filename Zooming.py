import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomPlus(image, factor):

    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)
    imgZoom = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y / factor)
            ori_x = int(x / factor)

            ori_y = min(ori_y, height - 1)
            ori_x = min(ori_x, width - 1)

            imgZoom[y, x] = image[ori_y, ori_x]

    return imgZoom

image = img.imread('D:\Kampus\SEMESTER 5\Pengolahan Citra Digital\Sesi 5 & 6\Horse.jpg')
skala = 2.0  # Faktor pembesaran 2x
imgZoom = zoomPlus(image, skala)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Gambar Asli")
plt.subplot(1, 2, 2)
plt.imshow(imgZoom)
plt.title("Gambar Diperbesar")
plt.show()