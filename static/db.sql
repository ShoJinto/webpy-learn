CREATE TABLE tdo (
  id serial primary key,
  title text,
  created timestamp default now(),
  done tinyint default 0    
  );


INSERT INTO tdo (title) VALUES ('Learn web.py');
