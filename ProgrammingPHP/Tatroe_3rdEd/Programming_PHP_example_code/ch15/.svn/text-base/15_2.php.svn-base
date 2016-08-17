<?php
class Book implements JsonSerializable
{
  public $id;
  public $name;
  public $edition;
  
  public function __construct($id)
  {
    $this->id = $id;
  }

  public function jsonSerialize()
  {
    $data = array(
      'id' => $this->id,
      'name' => $this->name,
      'edition' => $this->edition
    );
    
    return $data;
  }
}

class Author implements JsonSerializable
{
  public $id;
  public $name;
  public $books = array();

  public function __construct($id)
  {
    $this->id = $id;
  }

  public function jsonSerialize()
  {
    $data = array(
      'id' => $this->id,
      'name' => $this->name,
      'books' => $this->books
    );
    
    return $data;
  }
}

class ResourceFactory
{
  static public function authorFromJson($jsonData)
  {
    $author = new Author($jsonData['id']);
    $author->name = $jsonData['name'];

    foreach ($jsonData['books'] as $bookIdentifier) {
      $this->books[] = new Book($bookIdentifier);
    }

    return $author;
  }

  static public function bookFromJson($jsonData)
  {
    $book = new Book($jsonData['id']);
    $book->name = $jsonData['name'];
    $book->edition = (int) $jsonData['edition'];

    return $book;
  }
}


?>