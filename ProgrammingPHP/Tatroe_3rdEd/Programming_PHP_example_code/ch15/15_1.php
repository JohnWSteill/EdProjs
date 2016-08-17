<?php
class Book
{
  public $id;
  public $name;
  public $edition;
  
  public function __construct($id)
  {
    $this->id = $id;
  }
}

class Author
{
  public $id;
  public $name;
  public $books = array();

  public function __construct($id)
  {
    $this->id = $id;
  }
}

?>