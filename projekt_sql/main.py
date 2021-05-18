import mysql.connector
# import funkcji menu
import operacje

baza = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dziennik"
)
kursor = baza.cursor()

operacje.wyswietl_menu()
wybor_sekcji = input("Co chcesz zrobic?\n")

while int(wybor_sekcji) != 0:
    ######################
    # CRUD dla przedmiotow
    ######################
    if int(wybor_sekcji) == 1:
        operacje.crud_przedmioty()
        operacje.wyswietl_menu()
        wybor_sekcji = input("Co chcesz zrobic?\n")

    elif int(wybor_sekcji) == 2:
        ######################
        # CRUD dla uczniow
        ######################
        operacje.crud_uczniowie()
        operacje.wyswietl_menu()
        wybor_sekcji = input("Co chcesz zrobic?\n")

    elif int(wybor_sekcji) == 3:
        ######################
        # CRUD dla nauczycieli
        ######################
        operacje.crud_nauczyciele()
        operacje.wyswietl_menu()
        wybor_sekcji = input("Co chcesz zrobic?\n")

    elif int(wybor_sekcji) == 4:
        ######################
        # CRUD dla ocen
        ######################
        operacje.crud_oceny()
        operacje.wyswietl_menu()
        wybor_sekcji = input("Co chcesz zrobic?\n")

    elif int(wybor_sekcji) == 5:
        ######################
        # CRUD dla uwag
        ######################
        operacje.crud_uwagi()
        operacje.wyswietl_menu()
        wybor_sekcji = input("Co chcesz zrobic?\n")

    elif int(wybor_sekcji) == 6:
        ######################
        # PROCEDURY
        ######################
        operacje.procedury()
        operacje.wyswietl_menu()
        wybor_sekcji = input("Co chcesz zrobic?\n")

    elif int(wybor_sekcji) == 0:
        print("Wyjscie z programu...\n")

    else:
        print("Bledny numer operacji. Wybierz nowy.\n")
        wybor_sekcji = input("Wybierz nowa operacje.\n")


print("Zakonczono prace programu.\n")

