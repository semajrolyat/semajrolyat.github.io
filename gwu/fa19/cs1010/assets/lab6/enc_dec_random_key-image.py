# This code encrypt & decrypt an image:
# 1. encryption method: add a uniform random generated float between [0, 1]
# to each pixel & mode 256; then decrypt
# 2. showing the results in a plot
# Date: Sep. 30th, 2019; Author: Shabnam Tafreshi

from PIL import Image
import numpy as np
import matplotlib
import random
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Include your SELFIE in the same folder as this M-file, and Replace with your own SELFIE
fig = plt.figure()

# Original Image
im = Image.open("myimage.png")
originalpix = np.array(im)
ax0 = fig.add_subplot(321)
ax0.set_title('Original Image', fontsize=9)
plt.imshow(originalpix)

#Gray image
im_gray = im.convert("L")
pix = np.array(im_gray, dtype="int16")
ax1 = fig.add_subplot(323)
ax1.set_title('Grayscale Image', fontsize=9)
plt.imshow(pix, cmap='gray')

# Key Image

k = np.zeros((pix.shape[0], pix.shape[1]))
for i in range(pix.shape[0]):
    for j in range(pix.shape[1]):
        k[i, j] = 255 * random.uniform(0, 1)


ax2 = fig.add_subplot(324)
ax2.set_title('Grayscale Key Image', fontsize=9)
plt.imshow(k, cmap='gray')

# Encryption
# =========== USE FOR LOOPS ================

for i in range(pix.shape[0]):
    for j in range(pix.shape[1]):
        pix[i, j] = (pix[i, j] + k[i, j]) % 256

ax3 = fig.add_subplot(325)
ax3.set_title('Decrypted Image', fontsize=9)
plt.imshow(pix, cmap='gray')

# Decryption
# =========== USE FOR LOOPS ================

for i in range(pix.shape[0]):
    for j in range(pix.shape[1]):
        pix[i, j] = (pix[i, j] - k[i, j]) % 256

ax3 = fig.add_subplot(326)
ax3.set_title('Encrypted Image', fontsize=9)
plt.imshow(pix, cmap='gray')

fig.savefig('enc_dec_random_key-image.png')
plt.show()
