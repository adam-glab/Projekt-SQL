# procedury, wyzwalacze, widoki

use dziennik;

#########################
# wyzwalacze
#########################

# zabezpieczenie przed wpisaniem blednej oceny
delimiter $$
create trigger ocena_aktualizacja
before update
on oceny for each row
begin
	declare blad varchar(255);
    set blad = 'Podano niewlasciwa ocene. Ocena nie moze byc wieksza od 6';
    if new.ocena > 6 then
		signal sqlstate '45000'
			set message_text=blad;
	end if;
end$$
delimiter ;

delimiter $$
create trigger ocena_wstawianie
before insert
on oceny for each row
begin
	declare blad varchar(255);
    set blad = 'Podano niewlasciwa ocene. Ocena nie moze byc wieksza od 6';
    if new.ocena > 6 then
		signal sqlstate '45000'
			set message_text=blad;
	end if;
end$$
delimiter ;

#drop trigger ocena_aktualizacja;
#drop trigger ocena_wstawianie;

#test
#insert into oceny values (12,9,'2021-04-05',1,1);
update oceny set ocena=9,data='2021-04-05',przedmiot=1,uczen=1 where id_oceny=1;
#########################
# widoki
#########################
#drop view kadra;
create view kadra as
select id_nauczyciela as 'ID',nazwisko,przedmioty.nazwa_przedmiotu as 'prowadzony przedmiot' from nauczyciele
inner join przedmioty on nauczyciele.przedmiot=przedmioty.id_przedmiotu
order by id_nauczyciela asc;

#drop view kadra;

#test
select * from kadra;

#########################
# procedury
#########################

# procedura wyswietla uwagi ucznia o ID podanym w argumencie

#drop procedure wykaz_uwag;
delimiter $$
create procedure wykaz_uwag(IN ucz_id SMALLINT)
begin
	select id_uwagi, nauczyciele.nazwisko as 'nazwisko nauczyciela',data,rodzaj,tresc from uwagi
	inner join nauczyciele on uwagi.nauczyciel=nauczyciele.id_nauczyciela
    inner join uczniowie on uwagi.uczen=uczniowie.id_ucznia
    where id_ucznia=ucz_id;
end$$
delimiter ;

#test
#call wykaz_uwag(1);

#########################

# procedura wyswietla oceny ucznia o danym ID w okreslony sposob:
# wejscie drugiego argumentu 0 -> ze wszystkich przedmiotow
# wejscie drugiego argumentu !=0  -> z przedmiotu o ID podanym w drugim argumencie

#drop procedure wykaz_ocen;
delimiter $$
create procedure wykaz_ocen(IN ucz_id SMALLINT, IN opcja SMALLINT)
begin
if opcja=0 then
	select id_oceny, ocena, przedmioty.nazwa_przedmiotu as 'przedmiot', data from oceny
    inner join uczniowie on oceny.uczen=uczniowie.id_ucznia
    inner join przedmioty on oceny.przedmiot=przedmioty.id_przedmiotu
    where id_ucznia=ucz_id;
    else if opcja>0 then
		select id_oceny, ocena, przedmioty.nazwa_przedmiotu as 'przedmiot', data from oceny
		inner join uczniowie on oceny.uczen=uczniowie.id_ucznia
		inner join przedmioty on oceny.przedmiot=przedmioty.id_przedmiotu
		where id_ucznia=ucz_id and id_przedmiotu=opcja;
	end if;
end if;    
end$$
delimiter ;

#test
#call wykaz_ocen(2,2);

#########################

# procedura wyswietla srednia oczen ucznia ze wszystkich przedmiotow

#drop procedure srednia_ucznia
delimiter $$
create procedure srednia_ucznia(IN ucz_id SMALLINT)
begin
	select przedmioty.nazwa_przedmiotu as 'przedmiot', avg(oceny.ocena) as 'srednia ocen' from oceny
	inner join przedmioty on przedmioty.id_przedmiotu=oceny.przedmiot
	inner join uczniowie on uczniowie.id_ucznia=oceny.uczen
	where id_ucznia=ucz_id
	group by przedmioty.nazwa_przedmiotu;
    
end$$
delimiter ;

#test
#call srednia_ucznia(3);

#########################

# procedura wyswietla srednia oczen klas ze wszystkich przedmiotow lub wybranego
# wejscie 0 -> wyswietl wszystkie przedmioty
# wejscie != 0 -> wyswietl przedmiot o ID podanym w argumencie

#drop procedure srednia_klas;
delimiter $$
create procedure srednia_klas(IN opcja SMALLINT)
begin
if opcja=0 then
	select uczniowie.klasa, przedmioty.nazwa_przedmiotu as 'przedmiot', avg(oceny.ocena) as 'srednia ocen' from oceny
	inner join przedmioty on przedmioty.id_przedmiotu=oceny.przedmiot
	inner join uczniowie on uczniowie.id_ucznia=oceny.uczen
	group by uczniowie.klasa, przedmioty.nazwa_przedmiotu
	order by uczniowie.klasa asc;
		else if opcja>0 then
			select uczniowie.klasa, przedmioty.nazwa_przedmiotu as 'przedmiot', avg(oceny.ocena) as 'srednia ocen' from oceny
			inner join przedmioty on przedmioty.id_przedmiotu=oceny.przedmiot
			inner join uczniowie on uczniowie.id_ucznia=oceny.uczen
			where id_przedmiotu=opcja
			group by uczniowie.klasa, przedmioty.nazwa_przedmiotu
			order by uczniowie.klasa asc;
		end if;
	end if;
end$$
delimiter ;

#test
#call srednia_klas(2);
