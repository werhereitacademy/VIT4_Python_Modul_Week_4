import kitap_işlemleri
import uye_işlemleri
import json


while True:
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

    secim_menu= input("Lütfen Bir seçim yapiniz:")

    if secim_menu == "1":
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
        uyelik_menu= input("Lütfen Bir seçim yapiniz:")
        if uyelik_menu=="1":
            pass
        elif uyelik_menu=="2":
            pass
        elif uyelik_menu=="3":
            pass
        elif uyelik_menu== "4":
            pass
        elif uyelik_menu=="5":
            pass
        elif uyelik_menu=="6":
            pass
        elif uyelik_menu == "7":
            pass
        elif uyelik_menu =="0":
            break

        
    elif secim_menu == "2":
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
        kitap_menu= input("Lütfen Bir seçim yapiniz:")
        
        if kitap_menu=="1":
            pass
        elif kitap_menu=="2":
            pass
        elif kitap_menu=="3":
            pass
        elif kitap_menu== "4":
            pass
        elif kitap_menu=="5":
            pass
        elif kitap_menu=="6":
            pass
        elif kitap_menu == "7":
            pass
        elif kitap_menu =="0":
            break
       
    elif secim_menu == "0":
        print("Cikis yaptiniz.")
        print("Tekrar Kütüphanemize bekleriz..")
        break
    else:
        print("Geçersiz seçim! Lütfen geçerli bir seçim yapınız.")


    