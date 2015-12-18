#!/usr/bin/perl 
#===============================================================================
#
#         FILE:  Ch2.1.circ.pl
#
#        USAGE:  ./Ch2.1.circ.pl  
#
#  DESCRIPTION:  Write a program that computes the circumference of a 
#  circle with a radius of 12.5. Circumference is 2π times the radius 
#  (approximately 2 times 3.141592654). The answer you get should be 
#  about 78.5. 
#  Modify the program from the previous exercise to prompt for and 
#  accept a radius from the person running the program. So, if the 
#  user enters 12.5 for the radius, she should get the same number 
#  as in the previous exercise.
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:  John Steill (jws), jsteill@morgridgfe.org
#      COMPANY:  Morgridge Instittue of Research
#      VERSION:  1.0
#      CREATED:  12/16/2015 14:32:29
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;
print " Enter num1 please: ";
chomp (my $num1 = <STDIN>);

print "\n Enter num2 please: ";
chomp (my $num2   = <STDIN>);

print "\n Product: ", $num1*$num2, "\n";

