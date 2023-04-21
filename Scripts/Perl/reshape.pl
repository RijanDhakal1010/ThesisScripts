#!/usr/bin/perl

use strict;
use warnings;

# Get input file name from command line argument
my $input_file = shift @ARGV;

# Open input file for reading
open my $in, "<", $input_file or die "Failed to open input file: $!";

# Read header row
my $header = <$in>;
chomp $header;

# Split header row into columns
my @headers = split /\t/, $header;

# For each row in input file, create a new file with row data
while (my $line = <$in>) {
  chomp $line;
  my @cols = split /\t/, $line;
  my $row = shift @cols;
  my $filename = "$row\_reshaped.tsv";
  open my $out, ">", $filename or die "Failed to open output file: $!";
  print $out "$headers[0]\t$row\n";
  for my $i (0 .. $#cols) {
    print $out "$headers[$i+1]\t$cols[$i]\n";
  }
  close $out;
}

# Close input file
close $in;

