#!/bin/sh

echo "observed_chr,predicted_chr,loss_of_coverage" > stats.csv
for (( c=1; c<=100; c++ ))
do
	python simulation.py
	perl -e 'while(<>){$c+=tr/|/|/};$c--;print "$c,"' queseq.fa >> stats.csv ; python mapping.py >> stats.csv
done
