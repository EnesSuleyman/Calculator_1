//Enes Süleyman Özkan
def Toplama(sayi1, sayi2):
    return sayi1 + sayi2

def Cikarma(sayi1, sayi2):
    return sayi1 - sayi2

def Carpma(sayi1, sayi2):
    return sayi1 * sayi2

def Bolme(sayi1, sayi2):
    return sayi1 * sayi2
  
print("\n***Kullanılabilecek Uygulamalar*** \n" \
        "1. Toplama\n" \
        "2. Cikarma\n" \
        "3. Carpma\n" \
        "4. Bolme\n")
  
  

select = int(input("Kullanmak istediğiniz uygulamayı seçiniz :\n"))

if select <= 4:
        deger_1 = int(input("İlk Değer: "))
        deger_2 = int(input("İkinci Değer: "))
        
        if select == 1:
            print(deger_1, "+", deger_2, "=",
                            Toplama(deger_1, deger_2))
        
        elif select == 2:
            print(deger_1, "-", deger_2, "=",
                            Cikarma(deger_1, deger_2))
        
        elif select == 3:
            print(deger_1, "*", deger_2, "=",
                            Carpma(deger_1, deger_2))
        
        elif select == 4:
            print(deger_1, "/", deger_2, "=",
                            Bolme(deger_1, deger_2))
else:
        print("Belirtilen değer aralığında bir uygulama seçilmemiştir")

