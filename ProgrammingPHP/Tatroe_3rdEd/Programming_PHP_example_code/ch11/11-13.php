<?php
$document = simplexml_load_file("books.xml");
foreach ($document->children() as $node) { 
	foreach ($node->attributes() as $attribute) {
		echo "{$attribute}\n"; 
	}
}