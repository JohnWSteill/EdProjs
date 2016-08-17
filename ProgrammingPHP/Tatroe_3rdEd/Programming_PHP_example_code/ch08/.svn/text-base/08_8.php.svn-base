<?php 
$conn = new Mongo() ;
$db = $conn->library ;
$authors = $db->authors ;

$author = array('authorid' => 1, 'name' => 'J.R.R. Tolkien');
$authors->insert($author) ;

$author = array('authorid' => 2, 'name' => 'Alex Haley');
$authors->insert($author) ;

$author = array('authorid' => 3, 'name' => 'Tom Clancy');
$authors->save($author) ;

$author = array('authorid' => 4, 'name' => 'Isaac Asimov');
$authors->save($author) ;

?>