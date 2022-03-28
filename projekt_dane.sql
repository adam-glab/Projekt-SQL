# plik zawiera informacje o rekordach wstawionych do poszczególnych tablic

use dziennik;
#select * from przedmioty;
#select * from uczniowie;
#select * from nauczyciele;
#select * from oceny;
#select * from uwagi;

insert into przedmioty values (1, 'Historia'),
(2,'Jezyk polski'),
(3,'WOS'),
(4,'Samoobrona'),
(5,'WF'),
(6,'Jezyk angielski');

insert into uczniowie values (1,'Jan','Nowak','IV'),
(2,'Marcin','Worstman','V'),
(3,'Anna','Mak','VI'),
(4,'Juliusz','Cezar','VI'),
(5,'Sebastian','Bastion','III');

insert into nauczyciele values (1,'Kiepski',3),
(2,'Grzyb',1),
(3,'Bochenek',4),
(4,'Kielbasa',5),
(5,'Zurek',6),
(6,'Jajko',2);

insert into oceny values(1,2,'2019-04-04',3,4),
(2,1,'2019-04-04',1,5),
(3,5,'2019-04-04',2,1),
(4,6,'2019-04-04',5,3),
(5,3,'2019-04-05',2,2),
(6,3,'2019-04-08',2,2),
(7,3,'2019-04-08',2,5),
(8,2,'2019-04-09',6,3),
(9,1,'2019-04-11',6,1),
(10,3,'2019-04-11',4,2);

insert into uwagi values (1,1,3,'2019-04-08',2,'Rzucanie krzeslami'),
(2,3,5,'2019-04-11',1,'Umycie tablicy'),
(3,3,2,'2019-04-13',1,'Posprzatanie sali'),
(4,3,1,'2019-04-15',2,'Wulgaryzmy'),
(5,2,1,'2019-04-15',1,'Namoczenie gabki'),
(6,2,4,'2019-04-16',2,'Krzyki na korytarzu');
