print(""" *** Hoşgeldiniz ***

Yapmak istediğiniz işlemi seçiniz.

 1- Bakiye Sorgulamak
 2- Para Yatırma
 3- Para Çekme 
 4- Kartı geri almak için ç' ye basınız.
 """)

bakiye=500

while True:
    islem=input("Yapmak istediğiniz işlem: ")
    if(islem=="ç" or islem=="Ç"):
        print("Yine bekleriz...")
        break
    elif (islem=="1"):
        print("Bakiyeniz {}'tldir.".format(bakiye))
    elif (islem=="2"):
        miktar= int(input("Yatırmak istediğiniz tutar: "))
        print("Yatırma istediğiniz tutar: {}'tldir.".format(miktar))
        karar= input("Para eklemek istiyorsanız E'ye istemiyorsanız H'ye basın.")
        if (karar=="E" or karar=="e"):
            eklenecekpara =int(input("Eklemek istediğiniz tutarı girin: "))
            yenitutar=miktar+eklenecekpara
            bakiye+=yenitutar
            print("İşlem Gerçekleştirildi.")
            print("Yeni bakiyeniz {}'tldir.".format(bakiye))
        else:
            bakiye+=miktar
            print("Yeni bakiyeniz {}'tldir.".format(bakiye))
    elif (islem=="3"):
        paracekme=int(input("Çekmek istediğiniz tutarı girin: "))
        if (paracekme>bakiye):
            print("Çekmek istediğiniz tutar bakiyenizi aşıyor.")
            continue
        bakiye-=paracekme
        print("İşlem Gerçekleştirildi.")
        print("Yeni bakiyeniz {}'tldir.".format(bakiye))
    else:
        print("Geçersiz işlem!!!")