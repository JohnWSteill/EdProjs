<?php 
function externalEntityReference($parser, $names, $base, $systemID, $publicID)
{
  if ($systemID) {
    if (!list ($parser, $fp) = createParser($systemID)) {
      echo "Error opening external entity {$systemID}\n";
      return false;
    }

    return parse($parser, $fp);
  }

  return false;
}

?>