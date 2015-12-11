CREATE TABLE todo (
  id serial primary key,
  title text,
  created timestamp default now(),
  done tinyint(1) default 0
  );

INSERT INTO todo (title) VALUES ('Learn web.py');