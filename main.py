import kitap_işlemleri
import uye_işlemleri
import json
import zaman


while True:
    try:
        print("""
    |=========Library  Management System=======[-][o][x]
    |        H a l k  K u t u p h a n e m i z e        |
    |              H O S  G E L D I N I Z              |
    |                                                  |
    |   1- UYELIK ISLEMLERI => 1                       |
    |   2- KITAP ISLEMLERI ==> 2                       |
    |   3- CIKIS ============> 0                       | 
    |                                                  |       
    |       copyright@vit4 group2  version 1.04        |
    |==================================================| """)

        ana_menu_secim= input("Lütfen Bir seçim yapiniz:")

        if ana_menu_secim == "1":
            print("""
    |=========Library  Management System=======[-][o][x]
    |        U Y E L I K   I S L E M L E R I N E       |
    |              H O S  G E L D I N I Z              |
    |                                                  |
    |   1- UYELER ====>1    5- KITAP ODUNC VERME=>5    |
    |   2- UYE EKLEME=>2    6- KITAP IADE =======>6    | 
    |   3- UYE ARA ===>3    7- KITAP TAKIBI =====>7    |
    |   4- UYE SIL ===>4    8- CIKIS ============>0    | 
    |                                                  | 
    |               version 1.04                       |       
    |           copyright@vit4 group2                  |
    |==================================================| """)
            menu_uye_islemleri= input("Lütfen Bir seçim yapiniz:")

            if menu_uye_islemleri=="1":
                pass

            elif menu_uye_islemleri=="2":
                uye_ekle(Uye_Adi,Tel,Adres)

            elif menu_uye_islemleri=="3":
                uye_ara(arama)

            elif menu_uye_islemleri== "4":
                uye_sil(silinecek_uye)

            elif menu_uye_islemleri=="5":
                kitap_odunc_verme()

            elif menu_uye_islemleri=="6":
                kitap_iade()

            elif menu_uye_islemleri == "7":
                pass
            elif menu_uye_islemleri =="0":
                print("Uye Islemlerinden cikis yaptiniz.")
                break
            else:
                print("Geçersiz seçim! Lütfen geçerli bir seçim yapınız.")

            
        elif ana_menu_secim == "2":
            print("""
    |=========Library  Management System=======[-][o][x]
    |        K I T A P   İ Ş L E M L E R İ N E         |
    |              H O Ş  G E L D İ N İ Z              |
    |                                                  |
    |   1- KITAPLAR ====>1    5- CIKIS===>0            |
    |   2- KITAP EKLEME=>2                             | 
    |   3- KITAP ARA ===>3                             |
    |   4- KITAP SIL ===>4                             | 
    |                                                  | 
    |               version 1.04                       |       
    |           copyright@vit4 group2                  |
    |==================================================| """)

            menu_kitap_islemleri= input("Lütfen Bir seçim yapiniz:")
            
            if menu_kitap_islemleri=="1":
                pass

            elif menu_kitap_islemleri=="2":
                kitap_ekle(Kitap_Adi, Yazar, Yayinevi, Barkod)

            elif menu_kitap_islemleri=="3":
                kitap_arama(arama)
            
            elif menu_kitap_islemleri== "4":
                kitap_sil(silinecek_veri)

            elif menu_kitap_islemleri =="0":
                print("Kitap Islemlerinden cikis yaptiniz.")
                break

            else:
                print("Geçersiz seçim! Lütfen geçerli bir seçim yapınız.")
        
        elif ana_menu_secim == "0":
            print("Cikis yaptiniz.")
            print("Tekrar Kütüphanemize bekleriz..")
            break

        else:
            print("Geçersiz seçim! Lütfen geçerli bir seçim yapınız.")


    except Exception as hata:
        print("Hata: ",hata, end="\n\n")


    