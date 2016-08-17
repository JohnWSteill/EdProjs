<?php
 if($_POST['bgcolor']) {
   setcookie('bgcolor', $_POST['bgcolor'], time() + (60 * 60 * 24 * 7));
 }

 if (isset($_COOKIE['bgcolor'])) {
   $bgcolor = $_COOKIE['bgcolor'];
 }
 else if (isset($_POST['bgcolor'])) {
   $bgcolor = $_POST['bgcolor'];
 }
 else {
   $bgcolor = "gray";
 }
?>

<body bgcolor="<?= $bgcolor ?>">

<form action="<?= $_SERVER['PHP_SELF'] ?>" method="POST">
  <select name="bgcolor">
    <option value="gray">Gray</option>
    <option value="white">White</option>
    <option value="black">Black</option>
    <option value="blue">Blue</option>
    <option value="green">Green</option>
    <option value="red">Red</option>
  </select>

  <input type="submit" />
</form>
</body>
