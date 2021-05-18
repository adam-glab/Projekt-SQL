import mysql.connector

baza = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dziennik"
)
kursor = baza.cursor()

def dodaj():
    print("Dodaj rekord do tablicy uwag.\n")
    u_uczen = input("Podaj ID ucznia:\n")
    u_nauczyciel = input("Podaj ID nauczyciela:\n")
    u_data = input("Podaj date otrzymania (RRRR-MM-DD):\n")
    u_rodzaj = input("Podaj rodzaj uwagi (1 -> Pozytywna, 2 -> Negatywna):\n")
    u_tresc = input("Podaj tresc uwagi:\n")
    try:
        kursor.execute(f"INSERT INTO uwagi(uczen,nauczyciel,data,rodzaj,tresc) VALUES ({u_uczen},{u_nauczyciel},'{u_data}',{u_rodzaj},'{u_tresc}')")
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
        kursor.execute("SELECT * FROM uwagi")
        print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
        for x in kursor:
            print(x)
    ############################
    # 2
    ############################
    elif int(wybor) == 2:
        print("1 -> wyszukaj po ID uwagi, 2 -> wyszukaj po ID ucznia, 3 -> wyszukaj po ID nauczyciela, 4 -> wyszukaj po dacie, 5 -> wyszukaj po rodzaju uwagi\n")
        wybor_kol = input("Podaj wybor:\n")
        ############################
        # 2.1
        ############################
        if int(wybor_kol) == 1:
            u_id = input("Podaj ID uwagi:\n")
            try:
                kursor.execute(f"SELECT * FROM uwagi WHERE id_uwagi LIKE {u_id}")
                print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.2
        ############################
        elif int(wybor_kol) == 2:
            u_przed_id = input("Podaj ID przedmiotu:\n")
            try:
                kursor.execute(f"SELECT * FROM uwagi WHERE przedmiot LIKE {u_przed_id}")
                print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.3
        ############################
        elif int(wybor_kol) == 3:
            u_ucz_id = input("Podaj ID ucznia:\n")
            try:
                kursor.execute(f"SELECT * FROM uwagi WHERE uczen LIKE {u_ucz_id}")
                print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.4
        ############################
        elif int(wybor_kol) == 4:
            u_data = input("Podaj date (RRRR-MM-DD):\n")
            try:
                kursor.execute(f"SELECT * FROM uwagi WHERE data LIKE '{u_data}'")
                print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.5
        ############################
        elif int(wybor_kol) == 5:
            u_rodzaj = input("Podaj rodzaj uwagi (1 -> Pozytywna, 2 -> Negatywna):\n")
            try:
                kursor.execute(f"SELECT * FROM uwagi WHERE rodzaj = {u_rodzaj}")
                print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        else:
            print("Wybrano niewlasciwy numer opcji.\n")
            return -1


def aktualizuj():
    print("Zaktualizuj dane uwagi.\n")
    print("1 -> wyszukaj po ID uwagi\n")
    print("2 -> wyszukaj po ID ucznia\n")
    print("3 -> wyszukaj po ID nauczyciela\n")
    print("4 -> wyszukaj po dacie\n")
    print("5 -> wyszukaj po rodzaju uwagi\n")
    wybor = input("Wybierz metode:\n")
    ############################
    # 1
    ############################
    if int(wybor) == 1:
        u_id = input("Podaj ID uwagi:\n")
        try:
            print("Znaleziono uwage:\n")
            kursor.execute(f"SELECT * FROM uwagi WHERE id_uwagi LIKE {u_id}")
            print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1
        nowy_uczen = input("Podaj ID ucznia:\n")
        nowy_nauczyciel = input("Podaj ID nauczyciela:\n")
        nowa_data = input("Podaj date otrzymania (RRRR-MM-DD):\n")
        nowy_rodzaj = input("Podaj rodzaj uwagi (1 -> Pozytywna, 2 -> Negatywna):\n")
        nowa_tresc = input("Podaj tresc uwagi:\n")
        try:
            kursor.execute(f"UPDATE uwagi SET uczen={nowy_uczen},nauczyciel={nowy_nauczyciel},data='{nowa_data}',rodzaj={nowy_rodzaj},tresc='{nowa_tresc}' WHERE id_uwagi LIKE {u_id}")
            baza.commit()
            print(f"Zaktualizowano rekord o ID {u_id}.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    ############################
    # 2
    # zostaje wyswietlona lista  1- lub wiecej- elementowa
    # uzytkownik musi wpisac ID uwagi (jezeli dany przedmiot ma wiele ocen - zostanie wybrana ocena o zadanym id uwagi)
    ############################
    elif int(wybor) == 2:
        u_uczen = input("Podaj ID ucznia:\n")
        try:
            print("Znaleziono uwage lub uwagi:\n")
            kursor.execute(f"SELECT * FROM uwagi WHERE uczen LIKE {u_uczen}")
            print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1

        lista_id = input("Wybierz ID uwagi:\n")
        nowy_uczen = input("Podaj ID ucznia:\n")
        nowy_nauczyciel = input("Podaj ID nauczyciela:\n")
        nowa_data = input("Podaj date otrzymania (RRRR-MM-DD):\n")
        nowy_rodzaj = input("Podaj rodzaj uwagi (1 -> Pozytywna, 2 -> Negatywna):\n")
        nowa_tresc = input("Podaj tresc uwagi:\n")
        try:
            kursor.execute(f"UPDATE uwagi SET uczen={nowy_uczen},nauczyciel={nowy_nauczyciel},data='{nowa_data}',rodzaj={nowy_rodzaj},tresc='{nowa_tresc}' WHERE id_uwagi LIKE {lista_id}")
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
        u_nauczyciel = input("Podaj ID nauczyciela:\n")
        try:
            print("Znaleziono uwage lub uwagi:\n")
            kursor.execute(f"SELECT * FROM uwagi WHERE nauczyciel LIKE {u_nauczyciel}")
            print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1

        lista_id = input("Wybierz ID uwagi:\n")
        nowy_uczen = input("Podaj ID ucznia:\n")
        nowy_nauczyciel = input("Podaj ID nauczyciela:\n")
        nowa_data = input("Podaj date otrzymania (RRRR-MM-DD):\n")
        nowy_rodzaj = input("Podaj rodzaj uwagi (1 -> Pozytywna, 2 -> Negatywna):\n")
        nowa_tresc = input("Podaj tresc uwagi:\n")
        try:
            kursor.execute(f"UPDATE uwagi SET uczen={nowy_uczen},nauczyciel={nowy_nauczyciel},data='{nowa_data}',rodzaj={nowy_rodzaj},tresc='{nowa_tresc}' WHERE id_uwagi LIKE {lista_id}")
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
        u_data = input("Podaj date:\n")
        try:
            print("Znaleziono uwage lub uwagi:\n")
            kursor.execute(f"SELECT * FROM uwagi WHERE data LIKE '{u_data}'")
            print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1

        lista_id = input("Wybierz ID uwagi:\n")
        nowy_uczen = input("Podaj ID ucznia:\n")
        nowy_nauczyciel = input("Podaj ID nauczyciela:\n")
        nowa_data = input("Podaj date otrzymania (RRRR-MM-DD):\n")
        nowy_rodzaj = input("Podaj rodzaj uwagi (1 -> Pozytywna, 2 -> Negatywna):\n")
        nowa_tresc = input("Podaj tresc uwagi:\n")
        try:
            kursor.execute(f"UPDATE uwagi SET uczen={nowy_uczen},nauczyciel={nowy_nauczyciel},data='{nowa_data}',rodzaj={nowy_rodzaj},tresc='{nowa_tresc}' WHERE id_uwagi LIKE {lista_id}")
            baza.commit()
            print(f"Zaktualizowano rekord o ID {lista_id}.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    ############################
    # 5
    # postepowanie analogiczne do #4, #3 i #2
    ############################
    elif int(wybor) == 5:
        u_rodzaj = input("Podaj rodzaj uwagi (1 -> Pozytywna, 2 -> Negatywna):\n")
        try:
            print("Znaleziono uwage lub uwagi:\n")
            kursor.execute(f"SELECT * FROM uwagi WHERE rodzaj = {u_rodzaj}")
            print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1

        lista_id = input("Wybierz ID uwagi:\n")
        nowy_uczen = input("Podaj ID ucznia:\n")
        nowy_nauczyciel = input("Podaj ID nauczyciela:\n")
        nowa_data = input("Podaj date otrzymania (RRRR-MM-DD):\n")
        nowy_rodzaj = input("Podaj rodzaj uwagi (1 -> Pozytywna, 2 -> Negatywna):\n")
        nowa_tresc = input("Podaj tresc uwagi:\n")
        try:
            kursor.execute(f"UPDATE uwagi SET uczen={nowy_uczen},nauczyciel={nowy_nauczyciel},data='{nowa_data}',rodzaj={nowy_rodzaj},tresc='{nowa_tresc}' WHERE id_uwagi LIKE {lista_id}")
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
    print("Usun uwagi z tablicy ocen.\n")
    u_id = input("Podaj id uwagi:\n")
    try:
        kursor.execute(f"DELETE FROM uwagi WHERE id_uwagi={u_id}")
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