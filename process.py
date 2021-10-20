from re import sub
from pylab import *
import numpy as np
import imageio
from skimage.io import imread
import matplotlib.pyplot as plt

a = imread("./test_images/a_frame/c000a.bmp")
b = imread("./test_images/a_frame/c001a.bmp")

figure(figsize=(12,10))
subplot(1,2,1)
imshow(a, cmap=cm.gray)
subplot(1,2,2)
imshow(b, cmap=cm.gray)

ia = a[:32,:32].copy()
ib = b[:32,:32].copy()

figure()
subplot(1,2,1)
imshow(ia, cmap=cm.gray)
subplot(1,2,2)
imshow(ib, cmap=cm.gray)

imshow(ib-ia, cmap=cm.gray)
title("Without Shift")