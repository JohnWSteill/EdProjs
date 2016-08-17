<?php
$timeZone = ini_get('date.timezone') ;
$dtz = new DateTimeZone($timeZone) ;

$start_dt 	= new DateTime("2009-02-12 16:42:33", $dtz);
$current_dt 		= new DateTime("now", $dtz);

// creates a new instance of TimeInterval
$dt_diff	= $start_dt->diff($current_dt) ; 

echo "The difference between: " . $start_dt->format("Y-m-d") 
. " and "  . $current_dt->format("Y-m-d") . " is " 
. $dt_diff->format('%y year(s), %m month(s), and %d day(s)');

?>