<?php
$document = simplexml_load_file("books.xml");
foreach ($document->book as $book) { 
	echo $book->title . "\r\n";
}