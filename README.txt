########## simulation.py ##########

Simulates the reference genome, query genome and the query scaffolds

Usage: python simulation.py

Output:
	1. refseq.fa - Simulated reference genome
	2. queseq.fa - Simulated query genome
	3. scfseq.fa - Simulated query scaffolds


########## mapping.py ##########

Aligns the query scaffolds to the reference genome and counts the number of pseudochromosomes for the query genome

Usage: python mapping.py

Output (console):
	The number of predicted chromosomes, Loss of coverage


########## run.sh ##########

Runs the simulation and mapping scripts for a 100 times to generate a statistical document giving the prediction accuracy

Usage: bash run.sh

Output:
	1. stats.csv - The number of chromosomes in the query genome, The number of predicted chromosomes, Loss of coverage
