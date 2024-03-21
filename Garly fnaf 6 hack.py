import os
import platform



def dil_secimi():
    if platform.system() != "Windows":
        print("Bu program yalnızca Windows 10 veya Windows 11'de çalışır. Lütfen uygun bir işletim sistemi kullanın.")
    elif platform.release() not in ["10", "11"]:
        print("Bu program yalnızca Windows 10 veya Windows 11'de çalışır. Lütfen uygun bir işletim sistemi sürümü kullanın.")
    else:
        os.system("cls")

    print("""lütfen bir dil seçin // please select a language
[1] türkçe
[2] English""")
    ww = input(">")
    if ww == "1":
        main_tr()
    elif ww == "2":
        main_ing()
    else:
        dil_secimi()







def main_tr():
    os.system("cls")
    menu = """Garly fnaf 6 hack 
[1] para hilesi
[2] gece hilesi"""    


    print(menu)
    w = input(">")
    if w == '1':
        def para_hilesi_tr():
            dosya_yolu = r"C:\Users\\User\\AppData\\Roaming\\MMFApplications\\fnaf6"
            try:
                with open(dosya_yolu, 'r') as dosya:
                    icerik = dosya.read()
                    money_index = icerik.find('money=')
                    if money_index != -1:
                        mevcut_money = icerik[money_index + len('money='):].split()[0]
                    else:
                        input("Data dosyasında para değeri bulunamadı. Menüye dönmek için enter'a basın.")
                        main_tr()
            except FileNotFoundError:
                input("Data dosya bulunamadı. Menüye dönmek için enter'a basın.")
                main_tr()
        
            try:
                yeni_money = int(input("Yeni para değerini girin: "))
                with open(dosya_yolu, 'r') as dosya:
                    icerik = dosya.read()
    
                index = icerik.find('money=')
                if index != -1:
                    sonraki_index = icerik.find('\n', index)
                    eski_night = icerik[index+len('money='):sonraki_index]
                    yeni_icerik = icerik.replace(f'money={eski_night}', f'money={yeni_money}')
    
                    with open(dosya_yolu, 'w') as dosya:
                        dosya.write(yeni_icerik)
    
                    input(f"Data başarıyla güncellendi. Menüye dönmek için enter'a basın (Para birimini güncellenmesi için oyunu yeniden başlatın).")
                    main_tr()
                else:
                    input("Data dosyasında gece değeri bulunamadı. Menüye dönmek için enter'a basın.")
                    main_tr()
            except FileNotFoundError:
                input("Data dosya bulunamadı. Menüye dönmek için enter'a basın.")
                main_tr()
            except ValueError:
                os.system("cls")
                print("""Garly fnaf 6 hack
[1] para hilesi
[2] gece hilesi
>1""")
                para_hilesi_tr()
        para_hilesi_tr()
            
    elif w == '2':
        def gece_hilesi_tr():

            dosya_yolu = r"C:\\Users\\User\\AppData\\Roaming\\MMFApplications\\fnaf6"
            try:
                with open(dosya_yolu, 'r') as dosya:
                    icerik = dosya.read()
                    night_index = icerik.find('night=')
                    if night_index != -1:
                        mevcut_night = icerik[night_index + len('night='):].split()[0]
                    else:
                        input("Data dosyasında gece değeri bulunamadı. Menüye dönmek için enter'a basın.")
                        main_tr()
            except FileNotFoundError:
                input("Data dosya bulunamadı. Menüye dönmek için enter'a basın.")
                main_tr()

        
            try:
                yeni_night = int(input("Yeni gece değerini girin (6 - 1 eğer daha az veya daha çok bir değer girerseniz oyun hata verebilir): "))
                with open(dosya_yolu, 'r') as dosya:
                    icerik = dosya.read()
    
                index = icerik.find('night')
                if index != -1:
                    sonraki_index = icerik.find('\n', index)
                    eski_night = icerik[index+len('night='):sonraki_index]
                    yeni_icerik = icerik.replace(f'night={eski_night}', f'night={yeni_night}')
    
                    with open(dosya_yolu, 'w') as dosya:
                        dosya.write(yeni_icerik)
    
                    input("Data başarıyla güncellendi. Menüye dönmek için enter tuşuna basın (gece nin güncelleme için oyunu yeniden başlatın).")
                    main_tr()
                else:
                    input("Data dosyasında gece değeri bulunamadı. Menüye dönmek için enter'a basın.")
                    main_tr()
            except FileNotFoundError:
                input("Data dosya bulunamadı. Menüye dönmek için enter'a basın.")
                main_tr()
            except ValueError:
                os.system("cls")
                print("""Garly fnaf 6 hack
[1] para hilesi
[2] gece hilesi
>1""")
                gece_hilesi_tr()
        gece_hilesi_tr()

        
    else:
        main_tr()

def main_ing():
    os.system("cls")
    menu = """Garly fnaf 6 hack 
[1] money cheat
[2] night cheat"""    


    print(menu)
    w = input(">")
    if w == '1':
        def para_hilesi_ing():

            dosya_yolu = r"C:\Users\\User\\AppData\\Roaming\\MMFApplications\\fnaf6"
            try:
                with open(dosya_yolu, 'r') as dosya:
                    icerik = dosya.read()
                    money_index = icerik.find('money=')
                    if money_index != -1:
                        mevcut_money = icerik[money_index + len('money='):].split()[0]
                    else:
                        input("No money value found in the data file. Press enter to return to the menu.")
                        main_ing()
            except FileNotFoundError:
                input("Data file not found. Press enter to return to the menu.")
                main_ing()
        
            try:
                yeni_money = int(input("Enter the new money value: "))
                with open(dosya_yolu, 'r') as dosya:
                    icerik = dosya.read()
    
                index = icerik.find('money=')
                if index != -1:
                    sonraki_index = icerik.find('\n', index)
                    eski_night = icerik[index+len('money='):sonraki_index]
                    yeni_icerik = icerik.replace(f'money={eski_night}', f'money={yeni_money}')
    
                    with open(dosya_yolu, 'w') as dosya:
                        dosya.write(yeni_icerik)
    
                    input(f"Data updated successfully Press enter to return to the menu (restart the game to update the currency).")
                    main_ing()
                else:
                    input("No night value found in the data file. Press enter to return to the menu.")
                    main_ing()
            except FileNotFoundError:
                input("Data file not found. Press enter to return to the menu.")
                main_ing()
            except ValueError:
                os.system("cls")
                print("""Garly fnaf 6 hack
[1] money cheat
[2] night cheat
>1""")
                para_hilesi_ing()
        para_hilesi_ing()
        
    elif w == '2':
        def gece_hilesi_ing():

            dosya_yolu = r"C:\\Users\\User\\AppData\\Roaming\\MMFApplications\\fnaf6"
            try:
                with open(dosya_yolu, 'r') as dosya:
                    icerik = dosya.read()
                    night_index = icerik.find('night=')
                    if night_index != -1:
                        mevcut_night = icerik[night_index + len('night='):].split()[0]
                    else:
                        input("No night value found in the data file. Press enter to return to the menu.")
                        main_ing()
            except FileNotFoundError:
                input("Data file not found. Press enter to return to the menu.")
                main_ing()


        
            try:
                yeni_night = int(input("Enter the new night value (6 - 1 if you enter a value more or less the game may give an error): "))
                with open(dosya_yolu, 'r') as dosya:
                    icerik = dosya.read()
    
                index = icerik.find('night')
                if index != -1:
                    sonraki_index = icerik.find('\n', index)
                    eski_night = icerik[index+len('night='):sonraki_index]
                    yeni_icerik = icerik.replace(f'night={eski_night}', f'night={yeni_night}')
    
                    with open(dosya_yolu, 'w') as dosya:
                        dosya.write(yeni_icerik)
    
                    input("Data updated successfully. Press enter to return to the menu (restart the game for the nightly update).")
                    main_ing()
                else:
                    input("No night value found in the data file. Press enter to return to the menu.")
                    main_ing()
            except FileNotFoundError:
                input("Data file not found. Press enter to return to the menu.")
                main_ing()
            except ValueError:
                os.system("cls")
                print("""Garly fnaf 6 hack
[1] money cheat
[2] night cheat
>2""")
                gece_hilesi_ing()
        gece_hilesi_ing()
    else:
        main_ing()

dil_secimi()

