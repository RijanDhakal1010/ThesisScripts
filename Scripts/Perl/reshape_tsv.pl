#!/usr/bin/perl
use strict;
use warnings;
use Text::CSV;

# Check for input file argument
if (@ARGV != 1) {
    print STDERR "Usage: $0 inputfile.tsv\n";
    exit 1;
}

my $input_file = $ARGV[0];

# Open input file
open(my $in_fh, '<', $input_file) or die "Could not open '$input_file': $!";

# Use Text::CSV to parse TSV
my $csv = Text::CSV->new({ sep_char => "\t", eol => "\n" });

# Read header row
my $header_row = $csv->getline($in_fh);
my @headers = @{$header_row};

# Process data rows
while (my $row = $csv->getline($in_fh)) {
    my $filename = $row->[0] . '_reshaped.tsv';
    open(my $out_fh, '>', $filename) or die "Could not open '$filename': $!";

    for (my $i = 0; $i < @headers; $i++) {
        my $header = $headers[$i];
        my $value = $row->[$i];
        $csv->print($out_fh, [$header, $value]);
    }

    close $out_fh;
}

# Close input file
close $in_fh;

