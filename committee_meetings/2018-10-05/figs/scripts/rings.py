import numpy as np
import matplotlib.pyplot as plt
import tifffile as tf
from strtens import dering
from time import perf_counter
from skimage import io, img_as_float

im1 = img_as_float(tf.imread(
    '../../../../../uCTdMRI/notes/2018-08-01-deringing/xray_bad_artifact.tif'))
im2 = img_as_float(tf.imread(
    '../../../../../uCTdMRI/notes/2018-08-01-deringing/recon_10122-8x.tif'))


x0 = 482
y0 = 476
M_rad = 300
M_azi = 300

t1 = perf_counter()
dering1 = dering.de_ring(im1, M_rad, M_azi, x0=x0, y0=y0)
t2 = perf_counter()

x0 = 610
y0 = 490
M_rad = 300
M_azi = 300

t3 = perf_counter()
dering2 = dering.de_ring(im2, M_rad, M_azi, x0=x0, y0=y0)
t4 = perf_counter()

io.imsave('../bad_rings.png', im1.astype('float16'))
io.imsave('../bad_rings_fixed.png', dering1.astype('float16'))
io.imsave('../med_rings.png', im2.astype('float16'))
io.imsave('../med_rings_fixed.png', dering2.astype('float16'))


# fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(15, 8))
# axtop, axbot = ax
# ax1, ax2 = axtop
# ax3, ax4 = axbot

# ax1.imshow(im1, cmap='gray')

# ax2.imshow(dering1, cmap='gray')
# ax2.set_title('{} seconds'.format(np.round(t2-t1, 3)))

# ax3.imshow(im2, cmap='gray')

# ax4.imshow(dering2, cmap='gray')
# ax4.set_title('{} seconds'.format(np.round(t4-t3, 3)))

# plt.tight_layout()
# plt.show()
