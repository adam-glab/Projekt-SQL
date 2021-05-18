import mysql.connector

baza = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dziennik"
)
kursor = baza.cursor()

def dodaj():
    print("Dodaj rekord do tablicy nauczycieli.\n")
    print("Tabela przedmiotow:\n")
    kursor.execute("SELECT * from przedmioty")
    print("ID | NAZWA PRZEDMIOTU\n")
    for x in kursor:
        print(x)
    n_nazwisko = input("\nPodaj nazwiwsko nauczyciela\n")
    n_numer = input("Podaj ID prowadzonego przedmiotu:\n")
    try:
        kursor.execute(f"INSERT INTO nauczyciele(nazwisko,przedmiot) VALUES ('{n_nazwisko}',{n_numer})")
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
    print("Tabela przedmiotow:\n")
    kursor.execute("SELECT * from przedmioty")
    print("ID | NAZWA PRZEDMIOTU\n")
    for x in kursor:
        print(x)
    wybor = input("Podaj metode wyswietlania:\n")
    ############################
    # 1
    ############################
    if int(wybor) == 1:
        kursor.execute("SELECT * FROM nauczyciele")
        print("ID | NAZWISKO | PRZEDMIOT\n")
        for x in kursor:
            print(x)
    ############################
    # 2
    ############################
    elif int(wybor) == 2:
        print("1 -> wyszukaj po ID nauczyciela, 2 -> wyszukaj po nazwisku nauczyciela, 3 -> wyszukaj po ID przedmiotu.\n")
        wybor_kol = input("Podaj wybor:\n")
        ############################
        # 2.1
        ############################
        if int(wybor_kol) == 1:
            n_id = input("Podaj ID nauczyciela:\n")
            try:
                kursor.execute(f"SELECT * FROM nauczyciele WHERE id_nauczyciela LIKE {n_id}")
                print("ID | NAZWISKO | PRZEDMIOT\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.2
        ############################
        elif int(wybor_kol) == 2:
            n_nazwisko = input("Podaj nazwisko:\n")
            try:
                kursor.execute(f"SELECT * FROM nauczyciele WHERE nazwisko LIKE {n_nazwisko}")
                print("ID | NAZWISKO | PRZEDMIOT\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.3
        ############################
        elif int(wybor_kol) == 3:
            n_p_id = input("Podaj ID przedmiotu:\n")
            try:
                kursor.execute(f"SELECT * FROM nauczyciele WHERE przedmiot LIKE {n_p_id}")
                print("ID | NAZWISKO | PRZEDMIOT\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        else:
            print("Wybrano niewlasciwy numer opcji.\n")
            return -1


def aktualizuj():
    print("Zaktualizuj nazwe nauczyciela.\n")
    print("Tabela przedmiotow:\n")
    kursor.execute("SELECT * from przedmioty")
    print("ID | NAZWA PRZEDMIOTU\n")
    for x in kursor:
        print(x)
    print("\n1 -> wyszukaj po ID\n")
    print("2 -> wyszukaj po nazwisku\n")
    wybor = input("Wybierz metode:\n")
    ############################
    # 1
    ############################
    if int(wybor) == 1:
        n_id = input("Podaj ID:\n")
        try:
            print("Znaleziono nauczyciela:\n")
            kursor.execute(f"SELECT * FROM nauczyciele WHERE id_nauczyciela LIKE {n_id}")
            print("ID | NAZWISKO | PRZEDMIOT\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1
        nowe_nazwisko = input("Podaj nowa nazwe nauczyciela:\n")
        nowy_przedmiot = input("Podaj nowy prowadzony przedmiot:\n")
        try:
            kursor.execute(f"UPDATE nauczyciele SET nazwisko='{nowe_nazwisko}',przedmiot={nowy_przedmiot} WHERE id_nauczyciela LIKE {n_id}")
            baza.commit()
            print(f"Zaktualizowano rekord o ID {n_id}.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    ############################
    # 2
    # zostaje wyswietlona lista nauczycieli 1- lub wiecej- elementowa
    # uzytkownik musi wpisac ID nauczyciela (na wypadek, gdyby bylo kilka osob o tym samym nazwisku - zostanie wybrany ten zadany)
    ############################
    elif int(wybor) == 2:
        n_nazwisko = input("Podaj nazwisko nauczyciela:\n")
        try:
            print("Znaleziono nauczyciela:\n")
            kursor.execute(f"SELECT * FROM nauczyciele WHERE nazwisko LIKE '{n_nazwisko}'")
            print("ID | NAZWISKO | PRZEDMIOT\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
        lista_id = input("Wybierz ID nauczyciela:\n")
        nowe_nazwisko = input("Podaj nowa nazwe nauczyciela:\n")
        nowy_przedmiot = input("Podaj nowy prowadzony przedmiot:\n")
        try:
            kursor.execute(f"UPDATE nauczyciele SET nazwisko='{nowe_nazwisko}',przedmiot={nowy_przedmiot} WHERE id_nauczyciela LIKE {lista_id}")
            baza.commit()
            print(f"Zaktualizowano rekord o ID {lista_id}.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    else:
        print("Wybrano niewlasciwy numer opcji.")
        return -1


def usun():
    print("Usun nauczyciela z tablicy nauczycieli.\n")
    n_id = input("Podaj id nauczyciela:\n")
    try:
        kursor.execute(f"DELETE FROM nauczyciele WHERE id_nauczyciela={n_id}")
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