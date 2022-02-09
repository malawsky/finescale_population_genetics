# fine-scale population structure using IBD sharing

## Overview

A pipeline to construct an IBD-based graph of an input population and use it for various applications

## Details

In population genetics, PCA is useful in tracking large-scale, common variant variation in a population. 
However, [common variant PCA is not always sufficient in revealing and controlling for fine-scale population structure](https://elifesciences.org/articles/61548).

In order to produce fine-scale representation of population architecture, I implemented a method to represent genetic relationships between individuals
using total IBD-sharing between individuals. This is done by constructing a graph where individuals are nodes and shared autosomal IBD segments are edges, weighted by the total length of IBD segments shared between two individuals. 

This code easily runs on 50,000 humans and has not been tested on larger sample sizes. This code runs in O(N²) time and file sizes scale at N² where N is the number of samples. Uses of this graph include but are not limited to:

1. Analyzing population structure using IBD-based clustering (example shown in population_structure.py).
2. As a fixed effect relationship matrix in association studies (can include relateds).
3. Conducting permutation tests in association studies by randomly permuting the outcome variable of high IBD-sharing individuals (e.g. randomly sample
the outcome variable from the 10 most highly weighted IBD-neighbors).

## Inputs and outputs

Input files are the seg IBIS output files. IBIS is a phase-free IBD detection algorithm with code available [here](https://github.com/williamslab/ibis).

Output files are:
1. sumIBD_all_chr_final.txt A (N*(N-1)/2)x3 table with the first and second columns as the IDs of every possible individual pairs and the third column the total length of IBD sharing in genetic units. (produced by total_sum.sh)
2. A Nx2 table with the first column an ID of an individual and the second column being a cluster designation bbased on Louvain graph clustering. (produced by louvain_cluster.py)



