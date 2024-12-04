import cv2
import numpy as np

resim=cv2.imread("kediresmi.jpg",0)#,0 resmi siyah beyaz yapar kanar 1 olur

cv2.imshow("logo1",resim)#resimi ekrana çıkartıyor


#print(resim)matrisel gösterimini verir
print(resim.size)#boyutu shapenin çarpımları bunu olusturur
print(resim.dtype)#hangi tipten olduğunu öğrenmek 
print(resim.shape)#genişliği yüksekliği kaç kanaldan oluştugunu gösterir

cv2.waitKey(0)

cv2.destrayAllMacos()
