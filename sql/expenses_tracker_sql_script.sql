-- create months table --
create table months (
	id int not null,
    name varchar(25) not null,
    primary key (id)
);

-- create income table -- 
-- create foreign key for month_id --
create table income (
	id int auto_increment not null,
    name varchar(255) not null,
    amount int not null,
    category varchar(255),
    date_time datetime not null default current_timestamp,
    month_id int not null,
    primary key (id),
    foreign key (month_id) references months (id)
) auto_increment=1;

-- create expenses table --
-- create foreign key for month_id --
create table expenses (
	id int auto_increment not null,
    name varchar(255) not null,
    amount int not null,
    category varchar(255),
    date_time datetime not null default current_timestamp,
    month_id int not null,
    note text,
    primary key (id),
    foreign key (month_id) references months (id)
) auto_increment=1;

-- insert values into months table --
insert into months
values 
	(1, 'January'), 
    (2, 'February'), 
    (3, 'March'), 
    (4, 'April'), 
    (5, 'May'), 
    (6, 'June'), 
    (7, 'July'), 
    (8, 'August'), 
    (9, 'September'), 
    (10, 'October'), 
    (11, 'November'), 
    (12, 'December')