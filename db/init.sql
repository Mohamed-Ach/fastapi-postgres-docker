create table post (
  id serial not null unique primary key,
  title varchar(256) not null,
  author varchar(64) not null,
  content text,
  date_created date default now()
);

insert into post(title,author,content)
values ('Hello World','PaNDoRa-s_AcToR','The obligatory Hello World Post ...'),
       ('Another Post','PaNDoRa-s_AcToR','Yet another blog post about something exciting');
