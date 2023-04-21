#!/usr/bin/perl

use strict;
use warnings;

# Check if a filename was provided; if not, print an error message and exit
if (@ARGV < 1) {
    print STDERR "Usage: $0 <filename>\n";
    exit 1;
}

my $input_filename = $ARGV[0];
my $output_filename = $input_filename . ".typed";

open(my $in_fh, '<', $input_filename) or die "Could not open file '$input_filename' $!";
open(my $out_fh, '>', $output_filename) or die "Could not open file '$output_filename' $!";

while (my $line = <$in_fh>) {
    chomp $line;
    my @fields = split('\t', $line);
    my $type = ($fields[0] =~ /[a-zA-Z]/) ? "species" : "Node";
    print $out_fh join("\t", $type, @fields) . "\n";
}

close($in_fh);
close($out_fh);

print "Output written to '$output_filename'\n";
