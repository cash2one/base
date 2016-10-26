drop table if exists entries;
create table entries(
	id integer primary key autoincreament,
	title string not null,
	text string not null

);
