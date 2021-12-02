import random

sayi= random.randint(1,100)

puan=100
hak=10
while hak>0:
   
    hak-=1
    sayi2=int(input("sayıyı tahmin et:"))
    if sayi2<sayi:
        print("yukarı çık")
        puan-=10
    elif sayi2>sayi:
        print("aşağı in") 
        puan-=10   
    elif sayi2==sayi:
        print("tebrikler kazandınız!!!")
        print("puanınız" + puan)
        break    
if hak==0:
    print("hakkınız bitti:(")