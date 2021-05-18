import mysql.connector

baza = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dziennik"
)
kursor = baza.cursor()

def dodaj():
    print("Dodaj rekord do tablicy uczniow.\n")
    u_imie = input("Podaj imie ucznia:\n")
    u_nazwisko = input("Podaj nazwisko ucznia:\n")
    u_klasa = input("Podaj klase ucznia:\n")
    try:
        kursor.execute(f"INSERT INTO uczniowie(imie,nazwisko,klasa) VALUES ('{u_imie}','{u_nazwisko}','{u_klasa}')")
        baza.commit()
        print("Wstawiono dane.\n")
    except:
        baza.rollback()
        print("Wystapil blad.\n")
        return -1


def wyswietl():
    print("W jaki sposob wyswietlic tablice?\n")
    print("1 -> pokaz cala tablice\n")
    print("2 -> pokaz konkretny rekord\n")
    wybor = input("Podaj metode wyswietlania:\n")
    ############################
    # 1
    ############################
    if int(wybor) == 1:
        kursor.execute("SELECT * FROM uczniowie")
        print("ID | IMIE | NAZWISKO | KLASA\n")
        for x in kursor:
            print(x)
    ############################
    # 2
    ############################
    elif int(wybor) == 2:
        print("1 -> wyszukaj po ID, 2 -> wyszukaj po nazwisku, 3 -> wyszukaj po klasie.\n")
        wybor_kol = input("Podaj wybor:\n")
        ############################
        # 2.1
        ############################
        if int(wybor_kol) == 1:
            u_id = input("Podaj ID ucznia:\n")
            try:
                kursor.execute(f"SELECT * FROM uczniowie WHERE id_ucznia LIKE {u_id}")
                print("ID | IMIE | NAZWISKO | KLASA\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.2
        ############################
        elif int(wybor_kol) == 2:
            u_nazwisko = input("Podaj nazwisko ucznia:\n")
            try:
                kursor.execute(f"SELECT * FROM uczniowie WHERE nazwisko LIKE '{u_nazwisko}'")
                print("ID | IMIE | NAZWISKO | KLASA\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.3
        ############################
        elif int(wybor_kol) == 3:
            u_klasa = input("Podaj klase ucznia:\n")
            try:
                kursor.execute(f"SELECT * FROM uczniowie WHERE klasa LIKE '{u_klasa}'")
                print("ID | IMIE | NAZWISKO | KLASA\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        else:
            print("Wybrano niewlasciwy numer opcji.\n")
            return -1


def aktualizuj():
    print("Zaktualizuj dane ucznia.\n")
    print("1 -> wyszukaj po ID\n")
    print("2 -> wyszukaj po nazwisku\n")
    print("3 -> wyszukaj po klasie\n")
    wybor = input("Wybierz metode:\n")
    ############################
    # 1
    ############################
    if int(wybor) == 1:
        u_id = input("Podaj ID:\n")
        try:
            print("Znaleziono ucznia:\n")
            kursor.execute(f"SELECT * FROM uczniowie WHERE id_ucznia LIKE {u_id}")
            print("ID | IMIE | NAZWISKO | KLASA\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1
        nowe_imie = input("Podaj nowe imie ucznia:\n")
        nowe_nazwisko = input("Podaj nowe nazwisko ucznia:\n")
        nowa_klasa = input("Podaj nowa klase ucznia:\n")
        try:
            kursor.execute(f"UPDATE uczniowie SET imie='{nowe_imie}',nazwisko='{nowe_nazwisko}',klasa='{nowa_klasa}' WHERE id_ucznia LIKE {u_id}")
            baza.commit()
            print(f"Zaktualizowano rekord o ID {u_id}.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    ############################
    # 2
    ############################
    elif int(wybor) == 2:
        u_nazwisko = input("Podaj nazwisko ucznia:\n")
        try:
            print("Znaleziono ucznia lub uczniow:\n")
            kursor.execute(f"SELECT * FROM uczniowie WHERE nazwisko LIKE '{u_nazwisko}'")
            print("ID | IMIE | NAZWISKO | KLASA\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1
        # zostaje wyswietlona lista uczniow 1- lub wiecej- elementowa
        # uzytkownik musi wpisac ID ucznia (na wypadek, gdyby bylo kilka osob o tym samym nazwisku - zostanie wybrany ten zadany)
        lista_id = input("Wybierz ID ucznia:\n")
        nowe_imie = input("Podaj nowe imie ucznia:\n")
        nowe_nazwisko = input("Podaj nowe nazwisko ucznia:\n")
        nowa_klasa = input("Podaj nowa klase ucznia:\n")
        try:
            kursor.execute(f"UPDATE uczniowie SET imie='{nowe_imie}',nazwisko='{nowe_nazwisko}',klasa='{nowa_klasa}' WHERE id_ucznia LIKE {lista_id}")
            baza.commit()
            print(f"Zaktualizowano rekord o ID {lista_id}.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    ############################
    # 3
    # postepowanie takie same jak w przypadku wyszukiwania nazwiskiem
    ############################
    elif int(wybor) == 3:
        u_klasa = input("Podaj klase ucznia:\n")
        try:
            print("Znaleziono ucznia lub uczniow:\n")
            kursor.execute(f"SELECT * FROM uczniowie WHERE klasa LIKE '{u_klasa}'")
            print("ID | IMIE | NAZWISKO | KLASA\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1
        lista_id = input("Wybierz ID ucznia:\n")
        nowe_imie = input("Podaj nowe imie ucznia:\n")
        nowe_nazwisko = input("Podaj nowe nazwisko ucznia:\n")
        nowa_klasa = input("Podaj nowa klase ucznia:\n")
        try:
            kursor.execute(f"UPDATE uczniowie SET imie='{nowe_imie}',nazwisko='{nowe_nazwisko}',klasa='{nowa_klasa}' WHERE id_ucznia LIKE {lista_id}")
            baza.commit()
            print(f"Zaktualizowano rekord o ID {lista_id}.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    else:
        print("Wybrano niewlasciwy numer opcji.\n")
        return -1


def usun():
    print("Usun ucznia z tablicy uczniow.\n")
    u_id = input("Podaj id ucznia:\n")
    try:
        kursor.execute(f"DELETE FROM uczniowie WHERE id_ucznia={u_id}")
        baza.commit()
        print("Skasowano rekord.\n")
    except:
        kursor.rollback()
        print("Wystapil blad.\n")
        return -1


#dodaj()
#wyswietl()
#aktualizuj()
#usun()