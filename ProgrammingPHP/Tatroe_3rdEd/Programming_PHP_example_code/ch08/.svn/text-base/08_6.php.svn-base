<?php
session_start();
$folder = $_SESSION['folder'];
$filename = $folder . "/question1.txt" ;

$file_handle = fopen($filename, "a+"); 
// open file for reading then clean it out
// pick up any text in the file that may already be there
$comments = fread($file_handle, filesize($filename));
fclose($file_handle); // close this handle

if (!empty($_POST['posted'])) {
    // create file if first time and then 
    //save text that is in $_POST['question1']
    $question1 = $_POST['question1'];
    $file_handle = fopen($filename, "w+"); 
    // open file for total overwrite

    if (flock($file_handle, LOCK_EX)) { 
        // do an exclusive lock
        if (fwrite($file_handle, $question1) == FALSE) {
            echo "Cannot write to file ($filename)";
        }
        flock($file_handle, LOCK_UN); 
        // release the lock
    }

    // close the file handle and redirect to next page ?
    fclose($file_handle);
    header( "Location: 08_7.php" );

} else {

?>
    <html>
    <head>
    <title>Files & folders - On-line Survey</title>
    </head>
    <body>

    <table border=0><tr><td>
    Please enter your response to the following survey question:
    </td></tr>
    <tr bgcolor=lightblue><td>
    What is your opinion on the state of the world economy?<br/> 
    Can you help us fix it ?
    </td></tr>
    <tr><td>
    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method=POST>
    <input type="hidden" name="posted" value=1>
    <br/>
    <textarea name="question1" rows=12 cols=35><?= $comments ?></textarea>
    </td></tr>
    <tr><td>
    <input type="submit" name="submit" value="Submit">
    </form></td></tr>
    </table>
<?php } ?>
