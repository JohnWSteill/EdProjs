<?php

$processor = new XsltProcessor;
$xsl = new DOMDocument; 
$xsl->load("rules.xsl"); 

$processor->importStyleSheet($xsl);

$xml = new DomDocument; 
$xml->load("feed.xml");
$result = $processor->transformToXml($xml);

echo "<pre>{$result}</pre>";