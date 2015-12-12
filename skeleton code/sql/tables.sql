CREATE TABLE items(
  id serial primary key,
  author_id int REFERENCES USER ,
  body text,
  creadted TIMESTAMP DEFAULT (CURRENT_TIMESTAMP at TIME ZONE 'utc')
)