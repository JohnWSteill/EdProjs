<?php
    // starting word
    $ms_word = new COM("word.application") or die("Unable to start Word app");
    echo "Found and Loaded Word, version {$ms_word->Version}\n";

    //open an empty document    
    $ms_word->Documents->Add();

    //do some weird stuff
    $ms_word->Selection->TypeText("Hello World");
    $ms_word->Documents[1]->SaveAs("c:/php_com_test.doc");

    //closing word
    $ms_word->Quit();

    //free the object
    $ms_word = null;
    
    echo "all done !" ;
    ?>

