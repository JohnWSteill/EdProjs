<?php
try {
	
  $handle = new PDO('mysql:host=localhost; dbname=banking_sys', 'petermac', 'abc123');
  // connection successful
} catch (Exception $e) {
	
  die("Connection failed: " . $e->getMessage());
}

try {  
	
  $handle->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $handle->beginTransaction();
  
  $handle->exec("insert into accounts (account_id, amount) values (23, '5000')" );
  $handle->exec("insert into accounts (account_id, amount) values (27, '-5000')" );
  
  $handle->commit();
  
} catch (Exception $e) {
	
  $handle->rollBack();
  echo "Transaction not completed: " . $e->getMessage();
}
?>
