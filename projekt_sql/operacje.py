import mysql.connector
import przedmioty
import uczniowie
import nauczyciele
import oceny
import uwagi

baza = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dziennik"
)
kursor = baza.cursor()


def wyswietl_menu():
    # menu uzytkownika
    print(":|MENU CRUD|:\n")
    print("1: PRZEDMIOTY\n")
    print("2: UCZNIOWIE\n")
    print("3: NAUCZYCIELE\n")
    print("4: OCENY\n")
    print("5: UWAGI\n")
    print("6: PROCEDURY\n")
    print("0: WYJSCIE\n")


def crud_przedmioty():
    print(":|PRZEDMIOTY|:\n")
    print("1: DODAJ\n")
    print("2: WYSWIETL\n")
    print("3: ZMODYFIKUJ\n")
    print("4: USUN\n")
    print("0: WROC\n")
    wybor_crud = input("Wybierz operacje.\n")
    while int(wybor_crud) != 0:
        if int(wybor_crud) == 1:
            przedmioty.dodaj()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 2:
            przedmioty.wyswietl()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 3:
            przedmioty.aktualizuj()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 4:
            przedmioty.usun()
            wybor_crud = input("Wybierz nowa operacje.\n")
        else:
            print("Bledny numer operacji. Wybierz nowy.\n")
            wybor_crud = input("Wybierz nowa operacje.\n")


def crud_uczniowie():
    print(":|UCZNIOWIE|:\n")
    print("1: DODAJ\n")
    print("2: WYSWIETL\n")
    print("3: ZMODYFIKUJ\n")
    print("4: USUN\n")
    print("0: WROC\n")
    wybor_crud = input("Wybierz operacje.\n")
    while int(wybor_crud) != 0:
        if int(wybor_crud) == 1:
            uczniowie.dodaj()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 2:
            uczniowie.wyswietl()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 3:
            uczniowie.aktualizuj()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 4:
            uczniowie.usun()
            wybor_crud = input("Wybierz nowa operacje.\n")
        else:
            print("Bledny numer operacji. Wybierz nowy.\n")
            wybor_crud = input("Wybierz nowa operacje.\n")


def crud_nauczyciele():
    print(":|NAUCZYCIELE|:\n")
    print("1: DODAJ\n")
    print("2: WYSWIETL\n")
    print("3: ZMODYFIKUJ\n")
    print("4: USUN\n")
    print("0: WROC\n")
    wybor_crud = input("Wybierz operacje.\n")
    while int(wybor_crud) != 0:
        if int(wybor_crud) == 1:
            nauczyciele.dodaj()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 2:
            nauczyciele.wyswietl()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 3:
            nauczyciele.aktualizuj()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 4:
            nauczyciele.usun()
            wybor_crud = input("Wybierz nowa operacje.\n")
        else:
            print("Bledny numer operacji. Wybierz nowy.\n")
            wybor_crud = input("Wybierz nowa operacje.\n")


def crud_oceny():
    print(":|OCENY|:\n")
    print("1: DODAJ\n")
    print("2: WYSWIETL\n")
    print("3: ZMODYFIKUJ\n")
    print("4: USUN\n")
    print("0: WROC\n")
    wybor_crud = input("Wybierz operacje.\n")
    while int(wybor_crud) != 0:
        if int(wybor_crud) == 1:
            oceny.dodaj()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 2:
            oceny.wyswietl()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 3:
            oceny.aktualizuj()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 4:
            oceny.usun()
            wybor_crud = input("Wybierz nowa operacje.\n")
        else:
            print("Bledny numer operacji. Wybierz nowy.\n")
            wybor_crud = input("Wybierz nowa operacje.\n")


def crud_uwagi():
    print(":|UWAGI|:\n")
    print("1: DODAJ\n")
    print("2: WYSWIETL\n")
    print("3: ZMODYFIKUJ\n")
    print("4: USUN\n")
    print("0: WROC\n")
    wybor_crud = input("Wybierz operacje.\n")
    while int(wybor_crud) != 0:
        if int(wybor_crud) == 1:
            uwagi.dodaj()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 2:
            uwagi.wyswietl()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 3:
            uwagi.aktualizuj()
            wybor_crud = input("Wybierz nowa operacje.\n")
        elif int(wybor_crud) == 4:
            uwagi.usun()
            wybor_crud = input("Wybierz nowa operacje.\n")
        else:
            print("Bledny numer operacji. Wybierz nowy.\n")
            wybor_crud = input("Wybierz nowa operacje.\n")

def procedury():
    print(":|PROCEDURY|:\n")
    print("1: Wykaz uwag ucznia\n")
    print("2: Wykaz ocen ucznia\n")
    print("3: Srednia ocen ucznia\n")
    print("4: Srednia klas\n")
    print("0: WROC\n")
    wybor_proc = input("Wybierz procedure.\n")
    while int(wybor_proc) != 0:

        ######################
        # wykaz_uwag(u_id) - zwraca liste uwag ucznia o id=u_id
        ######################

        if int(wybor_proc) == 1:
            u_id = input("Podaj ID ucznia:\n")
            ######################
            # wywolanie procedury i przekazanie listy argumentow
            ######################
            kursor.callproc('wykaz_uwag', [int(u_id), ])
            print("ID uwagi | UCZEN | NAUCZYCIEL | DATA | RODZAJ | TRESC\n")
            ######################
            # wypisanie przechowywanych danych
            ######################
            for x in kursor.stored_results():
                print(x.fetchall())
            wybor_proc = input("Wybierz procedure.\n")

        ######################
        # wykaz_ocen(u_id, p_id) - zwraca liste ocen ucznia o id=u_id:
        # gdy p_id=0 -> wyswietla wszystkie oceny,
        # gdy p_id>0 -> wyswietla oceny z przedmiotu o id=p_id
        ######################

        elif int(wybor_proc) == 2:
            u_id = input("Podaj ID ucznia:\n")
            p_id = input("Podaj ID przedmiotu. Wybranie '0' spowoduje wyswietlenie wszystkich ocen:\n")
            kursor.callproc('wykaz_ocen', [int(u_id), int(p_id)])
            print("ID Oceny | OCENA | PRZEDMIOT | DATA\n")
            for x in kursor.stored_results():
                print(x.fetchall())
            wybor_proc = input("Wybierz procedure.\n")

        ######################
        # srednia_ucznia(u_id) - zwraca liste srednich ocen ucznia id=u_id z kazdego przedmiotu
        ######################

        elif int(wybor_proc) == 3:
            u_id = input("Podaj ID ucznia:\n")
            kursor.callproc('srednia_ucznia', [int(u_id), ])
            print("PRZEDMIOT | SREDNIA OCEN\n")
            for x in kursor.stored_results():
                print(x.fetchall())
            wybor_proc = input("Wybierz procedure.\n")

        ######################
        # srednia_klas(opcja)
        # opcja=0 - wyswietla srednia wszystkich klas ze wszystkich przedmiotow,
        # #opcja>0 - wyswietla srednia klas z przedmiotu o id=opcja
        ######################

        elif int(wybor_proc) == 4:
            opcja = input("Podaj ID przedmiotu. Wybranie '0' wyswietli srednie ze wszystkich przedmiotow:\n")
            kursor.callproc('srednia_klas', [int(opcja), ])
            print("KLASA | PRZEDMIOT | SREDNIA OCEN\n")
            for x in kursor.stored_results():
                print(x.fetchall())
            wybor_proc = input("Wybierz procedure.\n")

        else:
            print("Bledny numer operacji. Wybierz nowy.\n")
            wybor_proc = input("Wybierz nowa operacje.\n")