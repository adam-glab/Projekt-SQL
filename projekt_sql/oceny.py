import mysql.connector

baza = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dziennik"
)
kursor = baza.cursor()

def dodaj():
    print("Dodaj rekord do tablicy ocen.\n")
    o_ocena = input("Podaj wartosc oceny:\n")
    o_data = input("Podaj date otrzymania (RRRR-MM-DD):\n")
    o_przedmiot = input("Podaj ID przedmiotu:\n")
    o_uczen = input("Podaj ID ucznia:\n")
    try:
        kursor.execute(f"INSERT INTO oceny(ocena,data,przedmiot,uczen) VALUES ({o_ocena},'{o_data}',{o_przedmiot},{o_uczen})")
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
        kursor.execute("SELECT * FROM oceny")
        print("ID OCENY | OCENA | DATA | PRZEDMIOT | UCZEN\n")
        for x in kursor:
            print(x)
    ############################
    # 2
    ############################
    elif int(wybor) == 2:
        print("1 -> wyszukaj po ID oceny, 2 -> wyszukaj po ID przedmiotu, 3 -> wyszukaj po ID ucznia, 4 -> wyszukaj po dacie, 5 -> wyszukaj po wartości oceny.\n")
        wybor_kol = input("Podaj wybor:\n")
        ############################
        # 2.1
        ############################
        if int(wybor_kol) == 1:
            o_oc_id = input("Podaj ID oceny:\n")
            try:
                kursor.execute(f"SELECT * FROM oceny WHERE id_oceny LIKE {o_oc_id}")
                print("ID OCENY | OCENA | DATA | PRZEDMIOT | UCZEN\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.2
        ############################
        elif int(wybor_kol) == 2:
            o_przed_id = input("Podaj ID przedmiotu:\n")
            try:
                kursor.execute(f"SELECT * FROM oceny WHERE przedmiot LIKE {o_przed_id}")
                print("ID OCENY | OCENA | DATA | PRZEDMIOT | UCZEN\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.3
        ############################
        elif int(wybor_kol) == 3:
            o_ucz_id = input("Podaj ID ucznia:\n")
            try:
                kursor.execute(f"SELECT * FROM oceny WHERE uczen LIKE {o_ucz_id}")
                print("ID OCENY | OCENA | DATA | PRZEDMIOT | UCZEN\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.4
        ############################
        elif int(wybor_kol) == 4:
            o_data = input("Podaj date (RRRR-MM-DD):\n")
            try:
                kursor.execute(f"SELECT * FROM oceny WHERE data LIKE '{o_data}'")
                print("ID OCENY | OCENA | DATA | PRZEDMIOT | UCZEN\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.5
        ############################
        elif int(wybor_kol) == 5:
            o_ocena = input("Podaj wysokosc oceny (1-6):\n")
            try:
                kursor.execute(f"SELECT * FROM oceny WHERE ocena LIKE {o_ocena}")
                print("ID OCENY | OCENA | DATA | PRZEDMIOT | UCZEN\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        else:
            print("Wybrano niewlasciwy numer opcji.\n")
            return -1


def aktualizuj():
    print("Zaktualizuj dane oceny.\n")
    print("1 -> wyszukaj po ID oceny\n")
    print("2 -> wyszukaj po ID przedmiotu\n")
    print("3 -> wyszukaj po ID ucznia\n")
    print("4 -> wyszukaj po dacie\n")
    wybor = input("Wybierz metode:\n")
    ############################
    # 1
    ############################
    if int(wybor) == 1:
        o_o_id = input("Podaj ID oceny:\n")
        try:
            print("Znaleziono oceny:\n")
            kursor.execute(f"SELECT * FROM oceny WHERE id_oceny LIKE {o_o_id}")
            print("ID OCENY | OCENA | DATA | PRZEDMIOT | UCZEN\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1
        nowa_ocena = input("Podaj nowa wartosc oceny:\n")
        nowy_uczen = input("Podaj nowe ID ucznia:\n")
        nowy_przedmiot = input("Podaj nowe ID przedmiotu:\n")
        nowa_data = input("Podaj nowa date (RRRR-MM-DD):\n")
        try:
            kursor.execute(f"UPDATE oceny SET ocena={nowa_ocena},data='{nowa_data}',przedmiot={nowy_przedmiot},uczen={nowy_uczen} WHERE id_oceny LIKE {o_o_id}")
            baza.commit()
            print(f"Zaktualizowano rekord o ID {o_o_id}.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    ############################
    # 2
    # zostaje wyswietlona lista ocen 1- lub wiecej- elementowa
    # uzytkownik musi wpisac ID oceny (jezeli dany przedmiot ma wiele ocen - zostanie wybrana ocena o zadanym id oceny)
    ############################
    elif int(wybor) == 2:
        o_przedmiot = input("Podaj ID przedmiotu:\n")
        try:
            print("Znaleziono ocene lub oceny:\n")
            kursor.execute(f"SELECT * FROM oceny WHERE przedmiot LIKE {o_przedmiot}")
            print("ID OCENY | OCENA | DATA | PRZEDMIOT | UCZEN\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1

        lista_id = input("Wybierz ID oceny:\n")
        nowa_ocena = input("Podaj nowa wartosc oceny:\n")
        nowy_uczen = input("Podaj nowe ID ucznia:\n")
        nowy_przedmiot = input("Podaj nowe ID przedmiotu:\n")
        nowa_data = input("Podaj nowa date (RRRR-MM-DD):\n")
        try:
            kursor.execute(f"UPDATE oceny SET ocena={nowa_ocena},data='{nowa_data}',przedmiot={nowy_przedmiot},uczen={nowy_uczen} WHERE id_oceny LIKE {lista_id}")
            baza.commit()
            print(f"Zaktualizowano rekord o ID {lista_id}.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    ############################
    # 3
    # postepowanie analogiczne do #2
    ############################
    elif int(wybor) == 3:
        o_uczen = input("Podaj ID ucznia:\n")
        try:
            print("Znaleziono ocene lub oceny:\n")
            kursor.execute(f"SELECT * FROM oceny WHERE uczen LIKE {o_uczen}")
            print("ID OCENY | OCENA | DATA | PRZEDMIOT | UCZEN\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1
        lista_id = input("Wybierz ID oceny:\n")
        nowa_ocena = input("Podaj nowa wartosc oceny:\n")
        nowy_uczen = input("Podaj nowe ID ucznia:\n")
        nowy_przedmiot = input("Podaj nowe ID przedmiotu:\n")
        nowa_data = input("Podaj nowa date (RRRR-MM-DD):\n")
        try:
            kursor.execute(f"UPDATE oceny SET ocena={nowa_ocena},data='{nowa_data}',przedmiot={nowy_przedmiot},uczen={nowy_uczen} WHERE id_oceny LIKE {lista_id}")
            baza.commit()
            print(f"Zaktualizowano rekord o ID {lista_id}.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    ############################
    # 4
    # postepowanie analogiczne do #3 i #2
    ############################
    elif int(wybor) == 4:
        o_data = input("Podaj date wystawienia oceny:\n")
        try:
            print("Znaleziono ocene lub oceny:\n")
            kursor.execute(f"SELECT * FROM oceny WHERE data LIKE '{o_data}'")
            print("ID OCENY | OCENA | DATA | PRZEDMIOT | UCZEN\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1
        lista_id = input("Wybierz ID oceny:\n")
        nowa_ocena = input("Podaj nowa wartosc oceny:\n")
        nowy_uczen = input("Podaj nowe ID ucznia:\n")
        nowy_przedmiot = input("Podaj nowe ID przedmiotu:\n")
        nowa_data = input("Podaj nowa date (RRRR-MM-DD):\n")
        try:
            kursor.execute(f"UPDATE oceny SET ocena={nowa_ocena},data='{nowa_data}',przedmiot={nowy_przedmiot},uczen={nowy_uczen} WHERE id_oceny LIKE {lista_id}")
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
    print("Usun oceny z tablicy ocen.\n")
    o_id = input("Podaj id oceny:\n")
    try:
        kursor.execute(f"DELETE FROM oceny WHERE id_oceny={o_id}")
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