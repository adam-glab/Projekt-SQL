create database if not exists dziennik;
use dziennik;
# tabela przedmiotow
create table if not exists przedmioty (
	id_przedmiotu SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    nazwa_przedmiotu VARCHAR(45),
    PRIMARY KEY (id_przedmiotu)
);

#tabela uczniow
create table if not exists uczniowie (
	id_ucznia SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    imie VARCHAR(45),
    nazwisko VARCHAR(45),
    klasa VARCHAR(3),
    PRIMARY KEY (id_ucznia)
);

#tabela nauczycieli
create table if not exists nauczyciele (
	id_nauczyciela SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	nazwisko VARCHAR(45) NOT NULL,
	przedmiot SMALLINT UNSIGNED,
    PRIMARY KEY (id_nauczyciela),
    FOREIGN KEY (przedmiot) REFERENCES przedmioty(id_przedmiotu)
);

#tabela ocen
drop table oceny;
create table if not exists oceny (
	id_oceny SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    ocena TINYINT UNSIGNED NOT NULL,
    data DATE,
    przedmiot SMALLINT UNSIGNED,
    uczen SMALLINT UNSIGNED,
    PRIMARY KEY (id_oceny),
    FOREIGN KEY (przedmiot) REFERENCES przedmioty(id_przedmiotu),
    FOREIGN KEY (uczen) REFERENCES uczniowie(id_ucznia)
);

#tabela uwag
create table if not exists uwagi(
	id_uwagi SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    uczen SMALLINT UNSIGNED,
    nauczyciel SMALLINT UNSIGNED,
    data DATE,
    rodzaj ENUM('Pozytywna','Negatywna'),
    tresc VARCHAR(50),
    PRIMARY KEY (id_uwagi),
	FOREIGN KEY (uczen) REFERENCES uczniowie(id_ucznia),
	FOREIGN KEY (nauczyciel) REFERENCES nauczyciele(id_nauczyciela)
);

create role if not exists 'admin_danych';
grant all on dziennik.* to 'admin_danych';

create role if not exists 'nauczyciel';
grant select on dziennik.* to 'nauczyciel';
grant insert, update, delete on dziennik.* to 'nauczyciel';
grant execute on dziennik.* to 'nauczyciel';

create user if not exists'kiepski'@localhost identified by 'kiepski1234'
password expire interval 180 day;
grant 'nauczyciel' to 'kiepski'@localhost;
alter user 'kiepski'@localhost with max_queries_per_hour 100;

