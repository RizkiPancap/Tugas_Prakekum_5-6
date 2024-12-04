## a. Mirroring untuk vertical dan horizontal dilakukan secara bersamaan

import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

path = 'D:\Kampus\SEMESTER 5\Pengolahan Citra Digital\Sesi 5 & 6\Horse.jpg'
image = img.imread(path)

flipped_horizontal = np.fliplr(image)
flipped_vertical = np.flipud(image)

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Gambar Asli")
plt.subplot(1, 3, 2)
plt.imshow(flipped_horizontal)
plt.title("Flip Horizontal")
plt.subplot(1, 3, 3)
plt.imshow(flipped_vertical)
plt.title("Flip Vertikal")
plt.show()