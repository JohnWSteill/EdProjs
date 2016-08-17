<?php
$timeZone = ini_get('date.timezone') ;
$dtz = new DateTimeZone($timeZone) ;

echo "Server's Time Zone: " . $timeZone . "<br/>";

foreach ( $dtz->getLocation() As $key => $value ){
	echo $key . " " . $value . "<br/>";
}

?>