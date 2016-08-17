<?php
function createParser($filename)
{
  $fh = fopen($filename, 'r');
  $parser = xml_parser_create();

  xml_set_element_handler($parser, "startElement", "endElement");
  xml_set_character_data_handler($parser, "characterData");
  xml_set_processing_instruction_handler($parser, "processingInstruction");
  xml_set_default_handler($parser, "default");

  return array($parser, $fh);
}

function parse($parser, $fh)
{
  $blockSize = 4 * 1024;  // read in 4 KB chunks

  while ($data = fread($fp, $blockSize)) {
    if (!xml_parse($parser, $data, feof($fp))) {
      // an error occurred; tell the user where
      echo 'Parse error: ' . xml_error_string($parser) . " at line " .
           xml_get_current_line_number($parser);

      return false;
    }
  }

  return true;
}

if (list ($parser, $fh) = createParser("test.xml")) {
  parse($parser, $fh);
  fclose($fh);

  xml_parser_free($parser);
}
