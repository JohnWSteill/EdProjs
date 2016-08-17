<?php
require("../fpdf/fpdf.php");

$pdf = new FPDF();
$pdf->AddPage();
$pdf->SetFont('Times','U',15);

$pdf->SetTextColor(128);
$pdf->Cell(0,5,'Times font, Underlined and shade of Grey Text',0,0,'L');
$pdf->ln();

$pdf->SetTextColor(255,0,0);
$pdf->Cell(0,5,'Times font, Underlined and Red Text',0,0,'L');
$pdf->Output();
?>
