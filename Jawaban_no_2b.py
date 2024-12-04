import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree, pivot='center'):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)
    height, width = image.shape[:2]
    max_dim = int(np.sqrt(height**2 + width**2))

    # Menangani gambar RGB (tanpa Alpha Channel)
    if image.shape[-1] == 3:
        extended_image = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)
    else:
        extended_image = np.zeros((max_dim, max_dim, 4), dtype=image.dtype)

    if pivot == 'center':
        origin_y, origin_x = height // 2, width // 2
        offset_y, offset_x = max_dim // 2, max_dim // 2
    elif pivot == 'top-left':
        origin_y, origin_x = 0, 0
        offset_y, offset_x = 0, 0
    else:
        raise ValueError("Pivot must be either 'center' or 'top-left'")

    for y in range(-origin_y, height - origin_y):
        for x in range(-origin_x, width - origin_x):
            newX = int(cos_deg * x - sin_deg * y) + offset_x
            newY = int(sin_deg * x + cos_deg * y) + offset_y
            if 0 <= newX < max_dim and 0 <= newY < max_dim:
                extended_image[newY, newX] = image[y + origin_y, x + origin_x]

    return extended_image

# Mengganti path ke file gambar Anda
image_path = 'D:/Kampus/SEMESTER 5/Pengolahan Citra Digital/Sesi 5 & 6/Horse.jpg'
# Membaca gambar
image = img.imread(image_path)

# Rotasi gambar
rotated_image_center = rotateImage(image, 45, pivot='center')
rotated_image_top_left = rotateImage(image, 45, pivot='top-left')

# Menampilkan hasil
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Gambar Asli")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(rotated_image_center)
plt.title("Rotasi dengan Pivot Center")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(rotated_image_top_left)
plt.title("Rotasi dengan Pivot Top-Left (0,0)")
plt.axis('off')

plt.show()
