[![wakatime](https://wakatime.com/badge/user/3c7a50f7-fbe6-44cd-bb8b-623bd7ce08b2/project/56fcd503-86b0-44d3-b04e-475aec8415a3.svg)](https://wakatime.com/badge/user/3c7a50f7-fbe6-44cd-bb8b-623bd7ce08b2/project/56fcd503-86b0-44d3-b04e-475aec8415a3)

# Particle Image Velocimetry

Parçacıklarının hareket yönlerinin tespit edilmesini hedeflemekteyim. Bunun için OpenPIV isimli kütüphaneden faydalanarak bir deneme yapacağım. Amacım kameradan elde ettiğim görüntüler arasında ikişerli gruplar oluşturarak bu iki resim arasındaki farklı tespit etmek. Bu sayede hangi parçaçık hangi yöne ne kadar ne hızla gitmiş tespitini yapmış olabileceğim.

Daha önceden kayıtlı olan iki resim üzerinde gerçekleştirdiğim test için [buraya](./main.ipynb) tıklayabilirsiniz.
Daha önceden kayıtlı olan resimleri kullanarak video şeklinde yaptığım inceleme için [buraya](./test.py) tıklayabilirsiniz.
Gerçek zamanlı olarak kameradan aldığım görüntüler üzerinden yaptığım inceleme için [buraya](#) tıklayabilirsiniz.

## Kısa Özet

![Test 1](./test_images/a_frame/c000a.bmp) ![Test 2](./test_images/a_frame/c001a.bmp)

---


![Output 1](./result/img_0.bmp) ![Output 2](./result/img_1.bmp)

---

<!-- blank line -->
<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="./result/img_0.bmp">
    <source src="./result/video/output.avi" type="video/avi">
  </video>
</figure>
<!-- blank line -->

## License
[MIT](LICENSE)
