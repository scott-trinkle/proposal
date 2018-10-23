import numpy as np
import tifffile as tf

print('Reading')
im = tf.imread('../../../../../uCTdMRI/data/xray/2018/recon_4x.tif')
print('Slicing')
im = im[1983:2420, 550:937, 624:1000]
print('Saving')
tf.imsave('recon_4x_segment.tif', im)

print('Clearing')
del im
