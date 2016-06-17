#!/usr/bin/perl 
#===============================================================================
#
#         FILE:  Ch3.1.ReverseStringList.pl
#
#        USAGE:  ./Ch3.1.ReverseStringList.pl  
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;


# Write a program that reads a list of strings (on separate lines) until end-of-input. Then it should print the strings in code point order. That is, if you enter the strings fred, barney, wilma, betty, the output should show barney betty fred wilma. Are all of the strings on one line in the output or on separate lines? Could you make the output appear in either style?
#
print "Please enter some names to sort:\n";
my @myStr = <STDIN>;
@myStr = sort @myStr;
print "\n         The Names: \n";
foreach (@myStr) {
    print "$_, " ;
}
print "\n";

