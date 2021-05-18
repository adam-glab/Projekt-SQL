import mysql.connector

baza = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dziennik"
)
kursor = baza.cursor()

def dodaj():
    print("Dodaj rekord do tablicy przedmiotow.\n")
    p_nazwa = input("Podaj nazwe przedmiotu\n")
    try:
        kursor.execute(f"INSERT INTO przedmioty(nazwa_przedmiotu) VALUES ('{p_nazwa}')")
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
        kursor.execute("SELECT * FROM przedmioty")
        print("ID | NAZWA PRZEDMIOTU\n")
        for x in kursor:
            print(x)
    ############################
    # 2
    ############################
    elif int(wybor) == 2:
        print("1 -> wyszukaj po ID, 2 -> wyszukaj po nazwie przedmiotu.\n")
        wybor_kol = input("Podaj wybor:\n")
        ############################
        # 2.1
        ############################
        if int(wybor_kol) == 1:
            p_id = input("Podaj ID przedmiotu:\n")
            try:
                kursor.execute(f"SELECT * FROM przedmioty WHERE id_przedmiotu LIKE {p_id}")
                print("ID | NAZWA PRZEDMIOTU\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        ############################
        # 2.2
        ############################
        elif int(wybor_kol) == 2:
            p_nazwa = input("Podaj nazwe przedmiotu:\n")
            try:
                kursor.execute(f"SELECT * FROM przedmioty WHERE nazwa_przedmiotu LIKE '{p_nazwa}'")
                print("ID | NAZWA PRZEDMIOTU\n")
                for x in kursor:
                    print(x)
            except:
                print("Wystapil blad.\n")
                return -1
        else:
            print("Wybrano niewlasciwy numer opcji.\n")
            return -1


def aktualizuj():
    print("Zaktualizuj nazwe przedmiotu.\n")
    print("1 -> wyszukaj po ID\n")
    print("2 -> wyszukaj po nazwie\n")
    wybor = input("Wybierz metode:\n")
    ############################
    # 1
    ############################
    if int(wybor) == 1:
        p_id = input("Podaj ID:\n")
        try:
            print("Znaleziono przedmiot:\n")
            kursor.execute(f"SELECT * FROM przedmioty WHERE id_przedmiotu LIKE {p_id}")
            print("ID | NAZWA PRZEDMIOTU\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad.\n")
            return -1
        nowa_nazwa = input("Podaj nowa nazwe przedmiotu:\n")
        try:
            kursor.execute(f"UPDATE przedmioty SET nazwa_przedmiotu='{nowa_nazwa}' WHERE id_przedmiotu LIKE {p_id}")
            baza.commit()
            print(f"Zaktualizowano rekord o ID {p_id}.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    ############################
    # 2
    ############################
    elif int(wybor) == 2:
        p_nazwa = input("Podaj nazwe przedmiotu:\n")
        try:
            print("Znaleziono przedmiot:\n")
            kursor.execute(f"SELECT * FROM przedmioty WHERE nazwa_przedmiotu LIKE '{p_nazwa}'")
            print("ID | NAZWA PRZEDMIOTU\n")
            for x in kursor:
                print(x)
        except:
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
        nowa_nazwa = input("Podaj nowa nazwe przedmiotu:\n")
        try:
            kursor.execute(f"UPDATE przedmioty SET nazwa_przedmiotu='{nowa_nazwa}' WHERE nazwa_przedmiotu LIKE '{p_nazwa}'")
            baza.commit()
            print("Zaktualizowano rekord.\n")
        except:
            baza.rollback()
            print("Wystapil blad. Nie zapisano zmian.\n")
            return -1
    else:
        print("Wybrano niewlasciwy numer opcji.")
        return -1


def usun():
    print("Usun przedmiot z tablicy przedmiotow.\n")
    p_id = input("Podaj id przedmiotu:\n")
    try:
        kursor.execute(f"DELETE FROM przedmioty WHERE id_przedmiotu={p_id}")
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