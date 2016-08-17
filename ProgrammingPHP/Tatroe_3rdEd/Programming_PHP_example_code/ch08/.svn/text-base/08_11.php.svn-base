<?php 
$conn = new Mongo() ;
$db = $conn->library ;
$authors = $db->authors ;

$data = $authors->findone( array('name' => 'Isaac Asimov'));

$books_array = array (
	array('ISBN' => '0-553-29337-0', 
		  'title' => 'Foundation', 
		  'pub_year' => 1951, 
		  'available' => 1 ), 
	array('ISBN' => '0-553-29438-5', 
		  'title' => 'I, Robot', 
		  'pub_year' => 1950, 
		  'available' => 1 ), 
	array('ISBN' => '0-517-546671', 
		  'title' => 'Exploring the Earth and the Cosmos', 
		  'pub_year' => 1982, 
		  'available' => 1 ),
	array('ISBN' => '0-553-29336-2', 
		  'title' => 'Second Foundation', 
		  'pub_year' => 1953, 
		  'available' => 1 )  )	;			

$authors->update(
	array('_id' => $data['_id']),
		array( '$set' =>
			array ('books' => $books_array )				
				)		
		);
?>