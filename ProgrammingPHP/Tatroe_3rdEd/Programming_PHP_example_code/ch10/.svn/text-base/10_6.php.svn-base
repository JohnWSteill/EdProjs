<?php

require("../../../fpdf/fpdf.php");

class myPDF extends FPDF
{

	//Page header
function Header()
	{
		global $title;

		$this->SetFont('Times','',12);
		$w = $this->GetStringWidth($title)+120;
		$this->SetDrawColor(0,0,180);
		$this->SetFillColor(230,0,230);
		$this->SetTextColor(0,0,255);
		$this->SetLineWidth(0.5);

		$this->Image('php-tiny.jpg',10,10.5,15,8.5);
		$this->Cell($w,9,$title,1,1,'C');
		$this->Ln(10);

	}

	//Page footer
function Footer()
	{
		//Position at 1.5 cm from bottom
		$this->SetY(-15);
		$this->SetFont('Arial','I',8);
		$this->Cell(0,10,'This is the page footer -> Page '.$this->PageNo().'/{nb}',0,0,'C');
	}

}

$title = "FPDF Library Page Header";

$pdf = new myPDF('P', 'mm', 'Letter');
$pdf->AliasNbPages();
$pdf->AddPage();
$pdf->SetFont('Times','',24);

$pdf->Cell(0,0,'some text at the top of the page',0,0,'L');
$pdf->ln(225);
$pdf->Cell(0,0,'More text toward the bottom',0,0,'C');

$pdf->AddPage();
$pdf->SetFont('Arial','B',15);

// Cell(W, H, 'text', Border, Return, 'Allign') - basic syntax
$pdf->Cell(0,0,'Top of page 2 after header',0,1,'C');

$pdf->Output();
?>