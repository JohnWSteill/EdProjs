<?php 
$conn = new Mongo() ;
$db = $conn->library ;
$authors = $db->authors ;

$data = $authors->findone( array('authorid' => 4));

echo 'Generated Primary Key: ' . $data['_id'] ;
echo "<br/>" ;
echo 'Author name: ' . $data['name'] ;
?>