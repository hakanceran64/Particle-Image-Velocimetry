from typing import final
import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt
import imageio
from time import sleep
from openpiv import tools, pyprocess, validation, filters, scaling

frame_a = []
frame_b = []
gray  = np.array([np.ones([512, 512]),    np.zeros([512, 512])],    dtype=np.uint8)

firstWord = ["./test_images/a_frame/c0", "./test_images/b_frame/c0"]
finalWord = ["a.bmp", "b.bmp"]
file_name = ["", ""]

## Figure'un RGB Array'e dönüştürülmesi.
def getFigureAsRGBArray(fig):
    fig.canvas.draw()
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    return img

# Dosya yollarının bir listeye kayıt edilmesi.
for i in range(0, 100, 1):
    if (i < 10):
        file_name[0] = (firstWord[0] + "0" + str(i) + finalWord[0])
        file_name[1] = (firstWord[1] + "0" + str(i) + finalWord[1])
        frame_a.append(file_name[0])
        frame_b.append(file_name[1])
    else:
        file_name[0] = (firstWord[0] + str(i) + finalWord[0])
        file_name[1] = (firstWord[1] + str(i) + finalWord[1])
        frame_a.append(file_name[0])
        frame_b.append(file_name[1])

# Görüntü işleme alanı.
for i in range(0, 99, 1):
    img_a = cv.imread(frame_a[i])
    img_b = cv.imread(frame_a[i+1])
    
    img_c = tools.imread(frame_a[i])

    gray[0] = cv.cvtColor(img_a, cv.COLOR_BGR2GRAY)
    gray[1] = cv.cvtColor(img_b, cv.COLOR_BGR2GRAY)
    
    # sleep(0.05)

    if (cv.waitKey(1) == ord("q")):
        cv.destroyAllWindows()
        print("Program Sonlandirildi.")
        break

# while False:    
    ## Processing
    winsize    = 32   # pixels, interrogation window size in frame A
    searchsize = 42   # pixels, search area size in frame B
    overlap    = 17   # pixels, 50% overlap
    dt         = 0.02 # sec, time interval between the two frames
    u0, v0, sig2noise = pyprocess.extended_search_area_piv(
        gray[0].astype(np.int32),
        gray[1].astype(np.int32),
        window_size=winsize,
        overlap=overlap,
        dt=dt,
        search_area_size=searchsize,
        sig2noise_method='peak2peak',
    )
    x, y = pyprocess.get_coordinates(image_size=gray[0].shape, search_area_size=searchsize, overlap=overlap)

    ## Post-processing
    u1, v1, mask = validation.sig2noise_val(u0, v0, sig2noise, threshold = 1.05)
    u2, v2 = filters.replace_outliers(u1, v1, method='localmean', max_iter=3, kernel_size=3)
    # convert x, y to mm
    # convert u, v to mm/sec
    x, y, u3, v3 = scaling.uniform(
        x, y, u2, v2,
        scaling_factor = 96.52,  # 96.52 pixels/millimeter
    )
    # 0,0 shall be bottom left, positive rotation rate is counterclockwise
    x, y, u3, v3 = tools.transform_coordinates(x, y, u3, v3)

    ## result
    tools.save(x, y, u3, v3, mask, 'exp1_001.txt' )
    fig, ax = plt.subplots(figsize=(8, 8))
    fig, ax = tools.display_vector_field(
        'exp1_001.txt',
        ax=ax,
        scaling_factor=100,
        scale=50, # scale defines here the arrow length
        width=0.0025, # width is the thickness of the arrow
        on_img=True, # overlay on the image
        image_name=frame_a[i],
    )

    sonuc = getFigureAsRGBArray(fig)

    cv.imshow("sonuc: ", sonuc)

    dosya_adi = "./result/img_" + str(i) + ".bmp"
    cv.imwrite(dosya_adi, sonuc)

    if (cv.waitKey(1) == ord("q")):
        cv.destroyAllWindows()
        print("Program Sonlandirildi.")
        break
