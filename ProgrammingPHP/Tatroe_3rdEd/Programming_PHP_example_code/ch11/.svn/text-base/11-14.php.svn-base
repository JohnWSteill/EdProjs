<?php
$document = simplexml_load_file("books.xml");
foreach ($document->children() as $book) { 
	$book->title = "New Title";
}

file_put_contents("BookList.xml", $document->asXml());