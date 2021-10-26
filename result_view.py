import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

# codec tanımlama ve VideoWriter nesnesi oluşturma bilgi için bkz: https://www.fourcc.org/codecs.php
fourcc = cv.VideoWriter_fourcc(*'XVID')

# Kaydedilecek video dosyasının adı, uzantısı, konumu, saniyedeki çerçeve sayısı ve çözünürlüğü
out = cv.VideoWriter('./result/video/output.avi', fourcc, 6.0, (800,800))

frame_a = []

firstWord = "./result/img_"
finalWord = ".bmp"
file_name = ""

# Dosya yollarının bir listeye kayıt edilmesi.
# frame_a
for i in range(0, 100, 1):
        file_name = (firstWord + str(i) + finalWord)
        frame_a.append(file_name)

# Görüntü işleme alanı.
for i in range(0, 99, 1):
    result_img = cv.imread(frame_a[i])

    cv.imshow("result_img: ", result_img)
    
    # sleep(0.1)
    
    # cv.flip(src, flipCode, dst) 2 boyutlu diziyi dikey yatay veya her iki eksen etrafında döndürür.
    # 0 => dikey döndürme
    # 1 => yatay döndürme
    # 2 => hem yatay hem dikey döndürme
    frame = cv.flip(result_img,1,dst=None)
 
    # Döndürülen görüntüyü video dosyasına yaz.
    out.write(result_img)

    if (cv.waitKey(1) == ord("q")):
        cv.destroyAllWindows()
        print("Program Sonlandirildi.")
        break
out.release()