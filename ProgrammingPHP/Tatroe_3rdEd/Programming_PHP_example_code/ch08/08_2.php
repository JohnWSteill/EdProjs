<?php 
$database = new SQLiteDatabase('c:/copy/library.sqlite');

$sql = "CREATE TABLE 'authors' ('authorid' INTEGER PRIMARY KEY, 'name' TEXT)";
         
if ($database->queryExec($sql, $error) == FALSE) {
		echo "Create Failure  - $error <br />" ;
} else {
	echo "Table Authors was created  <br />" ;
}

$sql = <<<SQL
INSERT INTO 'authors' ('name') VALUES ('J.R.R. Tolkien');
INSERT INTO 'authors' ('name') VALUES ('Alex Haley');
INSERT INTO 'authors' ('name') VALUES ('Tom Clancy');
INSERT INTO 'authors' ('name') VALUES ('Isaac Asimov');
SQL;
 
if ($database->queryExec($sql, $error) == FALSE) {
	echo "Insert Failure  - $error <br />" ;
} else {
	echo "INSERT to  Authors - OK  <br />" ;
}
?>