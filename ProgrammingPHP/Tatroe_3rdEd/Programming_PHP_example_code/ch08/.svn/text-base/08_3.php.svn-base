<?php 
$database = new SQLiteDatabase('c:/copy/library.sqlite');

$sql = "CREATE TABLE 'books' ('bookid' INTEGER PRIMARY KEY, 
		'authorid' INTEGER,
		'title' TEXT,
		'ISBN' TEXT,
		'pub_year' INTEGER,
		'available' INTEGER)";

if ($database->queryExec($sql, $error) == FALSE) {
	echo "Create Failure  - $error <br />" ;
} else {
	echo "Table Books was created  <br />" ;
}

$sql = <<<SQL
INSERT INTO books ('authorid', 'title', 'ISBN', 'pub_year', 'available') 
VALUES (1, 'The Two Towers', '0-261-10236-2', 1954, 1);

INSERT INTO books ('authorid', 'title', 'ISBN', 'pub_year', 'available') 
VALUES (1, 'The Return of The King', '0-261-10237-0', 1955, 1);

INSERT INTO books ('authorid', 'title', 'ISBN', 'pub_year', 'available') 
VALUES (2, 'Roots', '0-440-17464-3', 1974, 1);
		
INSERT INTO books ('authorid', 'title', 'ISBN', 'pub_year', 'available') 
VALUES (4, 'I, Robot', '0-553-29438-5', 1950, 1);
				
INSERT INTO books ('authorid', 'title', 'ISBN', 'pub_year', 'available') 
VALUES (4, 'Foundation', '0-553-80371-9', 1951, 1); 
SQL;

if ($database->queryExec($sql, $error) == FALSE) {
	echo "Insert Failure  - $error <br />" ;
} else {
	echo "INSERT to  Books - OK  <br />" ;
}
?>