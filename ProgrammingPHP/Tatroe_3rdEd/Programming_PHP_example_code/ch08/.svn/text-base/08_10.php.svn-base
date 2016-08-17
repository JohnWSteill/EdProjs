<?php 
$conn = new Mongo() ;
$db = $conn->library ;
$authors = $db->authors ;

$authors->update(
	array('name' => 'Isaac Asimov'),
	array( '$set' =>
		array ('books' =>
			array ('0-425-17034-9' => 'Foundation', 
				   '0-261-10236-2' => 'I, Robot', 
				   '0-440-17464-3' => 'Second Foundation',
				   '0-425-13354-0' => 'Pebble In The Sky')					
			)				
		)		
	);
?>