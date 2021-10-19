from openpiv import tools, pyprocess, validation, filters, scaling
import sys 
sys.path.append('/usr/local/lib/python3.8/site-packages')
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import imageio

# Reading Images
# frame_a = mpimg.imread("./test_images/a_frame/c002a.bmp")
# frame_b = mpimg.imread("./test_images/a_frame/c003a.bmp")

# plt.imshow(frame_a)

#fig, ax = plt.subplots(1, 2, figsize = (12,10))

#ax[0].imshow(frame_a, cmap = plt.cm.gray)
#ax[1].imshow(frame_b, cmap = plt.cm.gray)

# plt.waitforbuttonpress()

print("Hello Word")

img = cv.imread(cv.samples.findFile("./test_images/a_frame/c000a.bmp"))
cv.imshow(img)

k = cv.waitKey(0)