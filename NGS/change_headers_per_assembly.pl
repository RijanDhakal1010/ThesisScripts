#!/usr/bin/perl

use strict;
use warnings;
use File::Basename;
use Getopt::Long;

my $file_extension;
my $pattern_word = "ID=";

GetOptions(
    "extension=s" => \$file_extension,
    "pattern_word=s" => \$pattern_word
) or die("Usage: $0 --extension <file_extension> --pattern_word <pattern_word>");

# Ensure required option is provided
unless (defined $file_extension) {
    die("Usage: $0 --extension <file_extension> --pattern_word <pattern_word>");
}

my $output_extension = 'new_' . $file_extension;

opendir my $dir, '.' or die "Cannot open directory: $!";

while (my $filename = readdir $dir) {

    next if ($filename !~ /$file_extension$/ || $filename =~ /^\./);

    my $input_file = './' . $filename;
    my $output_file = './' . basename($filename, $file_extension) . $output_extension;

    open my $in_fh, '<', $input_file or die "Cannot open file: $!";
    open my $out_fh, '>', $output_file or die "Cannot create file: $!";

    while (my $line = <$in_fh>) {

        if ($line =~ /($pattern_word\S+)/) {

            my $id = $1;

            $line =~ s/.*/>${id}/;
        }

        print $out_fh $line;
    }

    close $in_fh;
    close $out_fh;
}

closedir $dir;

