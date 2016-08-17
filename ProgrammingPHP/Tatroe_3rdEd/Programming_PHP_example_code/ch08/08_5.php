<?php 
error_reporting(E_ALL);
ini_set("display_errors", 1);
session_start();
if (!empty($_POST['posted']) && !empty($_POST['email'])) {

    $folder = "surveys/" . strtolower($_POST['email']);

    // send path information to the session
    $_SESSION['folder'] = $folder;

    if (!file_exists($folder)) {
        // make the directory and then add the empty files
        mkdir($folder, 0777, true);
    }

    header( "Location: 08_6.php" );

 } else {  ?>
     <html>
     <head>
     <title>Files & folders - On-line Survey</title>
     </head>
     <body bgcolor="#FFFFFF" text="#000000">
     <h2>Survey Form </h2>
     <p>Please enter your e-mail address to start recording your comments</p>
     <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method=POST>
     <input type="hidden" name="posted" value=1>
     <p>e-mail address: <input type="text" name="email" size="45" >
     <br/><br/>
     <input type="submit" name="submit" value="Submit">
     </form>

<?php } ?>

</body>
</html> 
