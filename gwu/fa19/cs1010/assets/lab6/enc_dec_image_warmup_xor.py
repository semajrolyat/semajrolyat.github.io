# This code encrypt & decrypt an image:
# 1. Encryption method: xor key to each pixel; then decrypt
# 2. Showing the results in a plot
# Date: Sep. 30th, 2019; Author: Shabnam Tafreshi

from PIL import Image
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Include your SELFIE in the same folder as this M-file
# And Replace with your own SELFIE

fig = plt.figure()

# Original Image
im = Image.open("lenna.png")
originalpix = np.array(im)
ax0 = fig.add_subplot(221)
ax0.set_title('Original Image', fontsize=9)
plt.imshow(originalpix)


# Gray Image
im2 = im.convert("L")
pix = np.array(im2)
ax1 = fig.add_subplot(222)
ax1.set_title('Grayscale Image', fontsize=9)
plt.imshow(pix, cmap='gray')

# Encryption
# =========== USE FOR LOOPS ================
# Change the key to see the changes
key = 150
for i in range(pix.shape[0]):
    for j in range(pix.shape[1]):
        pix[i, j] = pix[i, j] ^ key

ax2 = fig.add_subplot(223)
ax2.set_title('Encrypted Image', fontsize=9)
plt.imshow(pix, cmap='gray')

# Decryption
# =========== USE FOR LOOPS ================

for i in range(pix.shape[0]):
    for j in range(pix.shape[1]):
        pix[i, j] = pix[i, j] ^ key

ax3 = fig.add_subplot(224)
ax3.set_title('Decrypted Image', fontsize=9)
plt.imshow(pix, cmap='gray')

fig.savefig('enc_dec_image_warmup_xor.png')
plt.show()

