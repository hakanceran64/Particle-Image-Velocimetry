[![wakatime](https://wakatime.com/badge/user/3c7a50f7-fbe6-44cd-bb8b-623bd7ce08b2/project/56fcd503-86b0-44d3-b04e-475aec8415a3.svg)](https://wakatime.com/badge/user/3c7a50f7-fbe6-44cd-bb8b-623bd7ce08b2/project/56fcd503-86b0-44d3-b04e-475aec8415a3)

## Quick Link

- [OpenPIV Read the Docs](https://openpiv.readthedocs.io/en/latest/index.html)
- [Particle image velocimetry - Wiki2](https://wiki2.org/en/Particle_image_velocimetry)
- [Open Source Particle Image Velocimetry](http://www.openpiv.net/)
- [PyPi Project OpenPIV 0.23.8](https://pypi.org/project/OpenPIV/)
- [alexlib GitHub ](https://github.com/alexlib/openpiv-python)
- [OpenPIV GitHub](https://github.com/OpenPIV)


# Particle Image Velocimetry

Parçacıklarının hareket yönlerinin tespit edilmesini hedeflemekteyim. Bunun için OpenPIV isimli kütüphaneden faydalanarak bir deneme yaptım. Amacım kameradan elde ettiğim görüntüler arasında ikişerli gruplar oluşturarak bu iki resim arasındaki farklı tespit etmek. Bu sayede hangi parçaçık hangi yöne ne kadar ne hızla gitmiş tespitini yapmış oldum.

Daha önceden kayıtlı olan iki resim üzerinde gerçekleştirdiğim test için [buraya](./main.ipynb) tıklayabilirsiniz.
Daha önceden kayıtlı olan resimleri kullanarak video şeklinde yaptığım inceleme için [buraya](./localPIV.py) tıklayabilirsiniz.
Gerçek zamanlı olarak kameradan aldığım görüntüler üzerinden yaptığım inceleme için [buraya](#) tıklayabilirsiniz.
Elde ettiğim görüntüleri ise [burada](./result_view.py) video formatında kaydettim.

## Kısa Özet

- [Giriş](./test_images/)

- [Sonuçlar](./result/)

<img src="./test_images/a_frame/c000a.bmp" width="400"> <br /> <img src="./result/img_0.bmp" width="400">

---

<video controls="controls">
  <source type="video/mp4" src="./result/video/output.mp4"></source>
  <source type="video/webm" src="./result/video/output.webm"></source>
  <p>Your browser does not support the video element.</p>
</video>

## License
[MIT](LICENSE)

---

## Made with ❤️ Python 