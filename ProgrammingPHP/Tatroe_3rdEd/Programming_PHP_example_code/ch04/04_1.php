<?php
// The Luhn checksum determines whether a credit card number is syntactically
// correct; it cannot, however, tell if a card with the number has been issued,
// is currently active, or has enough space left to accept a charge.

function IsValidCreditCard($cardNumber, $cardType)
{
  // Assume it's okay
  $isValid = true;

  // Strip all non-numbers from the string
  $cardNumber = ereg_replace('[^[:digit:]]','', $cardNumber);

  // Make sure the card number and type match
  switch($cardType) {
    case 'mastercard':
      $isValid = ereg('^5[1-5].{14}$', $cardNumber);
    break;

    case 'visa':
      $isValid = ereg('^4.{15}$|^4.{12}$', $cardNumber);
    break;

    case 'amex':
      $isValid = ereg('^3[47].{13}$', $cardNumber);
    break;

    case 'discover':
      $isValid = ereg('^6011.{12}$', $cardNumber);
    break;

    case 'diners':
      $isValid = ereg('^30[0-5].{11}$|^3[68].{12}$', $cardNumber);
    break;

    case 'jcb':
      $isValid = ereg('^3.{15}$|^2131|1800.{11}$', $cardNumber);
    break;
  }

  // It passed the rudimentary test; let's check it against the Luhn this time
  if ($isValid) {
    // Work in reverse
    $cardNumber = strrev($cardNumber);

    // Total the digits in the number, doubling those in odd-numbered positions
    $total = 0;

    for ($i = 0; $i < strlen($cardNumber); $i++) {
      $adder = (int) $cardNumber[$i];

      // Double the numbers in odd-numbered positions
      if ($i % 2) {
        $adder = $adder << 1;

        if ($adder > 9) {
          $adder -= 9;
        }
      }
    }

    $total += $adder;
  }

  // Valid cards will divide evenly by 10
  $isValid = (($total % 10) == 0);

  return $isValid;
}

?>