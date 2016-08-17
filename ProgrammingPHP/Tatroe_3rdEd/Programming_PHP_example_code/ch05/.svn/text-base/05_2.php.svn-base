<?php
$extraData = array("border" => 2, "color" => 'red');
$baseArray = array('Ford', 'Crysler', 'VW', 'Honda', 'Toyota');
array_walk($baseArray, 'WalkFunction', $extraData);

function WalkFunction($item, $index, $data)
{
    echo $item . " <- item, then border: " . $data['border']; 
    echo " color->" . $data['color'] . "<br />" ;   
}
?>