import time # Programın en sonunda 5 saniye beklemesi için time modulü import ettim
while True:  # Sonsuz döngü
    print("Toplama için 1")
    print("Çıkarma için 2")
    print("Çarpma için 3")
    print("Bölme için 4")
    print("")

    z = int(input("Bu sayılardan birini giriniz. "))  # İşlem türü seçimi için
    if z in [1, 2, 3, 4]:  # Eğer z 1, 2, 3 veya 4 ise döngüye gir
        x = int(input("İlk sayıyı giriniz. "))  # İlk sayıyı tam sayıya çevir
        y = int(input("İkinci sayıyı giriniz. "))  # İkinci sayıyı tam sayıya çevir

        print(x)  # İlk sayıyı yazdır
        print(y)  # İkinci sayıyı yazdır

        # İşlemleri gerçekleştir
        if z == 1:
            print(x + y)  # Toplama işlemi
        elif z == 2:
            print(x - y)  # Çıkarma işlemi
        elif z == 3:
            print(x * y)  # Çarpma işlemi
        elif z == 4:
            print(x / y)  # Bölme işlemi
            
        time.sleep(5)
        break  # Döngüden çık
    else:
        print("")
        print("Geçersiz giriş yaptınız, lütfen tekrar deneyin.")
        print("")
time.sleep(5) # İşlemler bittiğinde 5 saniye beklemesi için