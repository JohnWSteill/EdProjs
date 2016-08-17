<?php
$authorId = 'ktatroe';
$url = "http://example.com/api/authors/{$authorId}";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);

$response = curl_exec($ch);
$resultInfo = curl_getinfo($ch);

curl_close($ch);

$authorJson = json_decode($response);
// decode the JSON using a Factory to instantiate an Author object
?>