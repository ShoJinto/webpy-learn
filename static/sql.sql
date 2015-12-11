CREATE TABLE todo (
  id serial primary key,
  title text,
  created timestamp default now(),
  done tinyint(1) default 0   
  );

INSERT INTO todo (title) VALUES ('Learn web.py');


$def with (tdos)

$if name:
    I Just wanted to say <em>Hello</em> to $name.
$else:
    <em>Hello</em>,webpy!


$def with(form)
<form name="main" method="post">
	$if not form.valid:
		<p class="error">Try again,AmeriCAN</p>
		$:form.render()
		<input type="submit" />
</form>