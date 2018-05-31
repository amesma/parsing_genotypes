#!/usr/bin/env python

#CS CM124
#Assignment: create a genotype parser for a recently admixed population to determins the haplotypes
#of individuals.

__author__ = "Jia Hui Ma"
__copyright__ = "2018"

import numpy as np

#load genome into program
#column is an individual
#row is a snp
def load_genome(file_name):
    gen = []
    f = open(file_name, 'r')
    for line in f:
        n = list(line.strip())
        gen.append(n)
    f.close()
    #need to rearrangel
    gen = np.array(gen, dtype=np.int8)
    gen = gen.transpose()
    return gen

def phase(matrix, result):
    current_hap = []
    total_hap = []
    delete = []

    for x in range(len(a)):
        line = a[x]
        for i in range(len(line)):
            if line[i] == 1:
                break
            elif line[i] == 0:
                current_hap.append(0)
            else:
                current_hap.append(1)
        if len(total_hap) == len(line):
            total_hap.append(current_hap)
            delete.append(x)
        current_hap = []
    total_hap = np.array(total_hap)
    #no need to check if haplotype is unique

def main():
    print load_genome("haplo_parse/sample_format.txt")

    #are there known haplotypes
if  __name__ =='__main__':
    main()
