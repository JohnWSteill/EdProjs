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


# Write a program that reads a list of numbers (on separate lines) until end-of-input and then prints for each number the corresponding person’s name from the list shown below. (Hardcode this list of names into your program. That is, it should appear in your program’s source code.) For example, if the input numbers were 1, 2, 4, and 2, the output names would be fred, betty, dino, and betty:
my @names = qw<fred betty barney dino wilma pebbles bamm-bamm>;
#
print "Please enter some numbers in (1,7):\n";
my @myStr = <STDIN>;
print "\n         The Names: \n";
foreach (@myStr) {
    print "$names[$_-1], " ;
}
print "\n"

