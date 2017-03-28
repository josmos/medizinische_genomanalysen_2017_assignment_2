#! /usr/bin/env python3

import numpy as np
import os
import subprocess
from cyvcf2 import VCF
import vcf

__author__ = 'Josef Moser'


class Assignment2:
    def __init__(self):
        if not os.path.isfile("AmpliseqExome.20141120.NA24385.vcf"):
            subprocess.call(["wget", "ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/data/"
                                     "AshkenazimTrio/analysis/IonTorrent_TVC_03162015/"
                                     "AmpliseqExome.20141120.NA24385.vcf"])
        self.vcf = "AmpliseqExome.20141120.NA24385.vcf"
        self.metadata = vcf.Reader(filename=self.vcf).metadata

    def get_average_quality_of_son(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''
        print("\nAverage PHRED Score is {}".format(np.mean([i.QUAL for i in VCF(self.vcf)])))

    def get_total_number_of_variants_of_son(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        print("\nNumber of Variants {}".format(len(list(VCF(self.vcf)))))

    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return:
        '''
        print("\nVariant Caller: {}".format(self.metadata["source"][0]))

    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return:
        '''
        print("\nReference Version: {}"
              .format(os.path.basename(self.metadata["reference"]).strip(".fasta")))
        
    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs 
        :return: 
        '''
        print("\nNumber of indels: {}"
              .format(sum([1 for i in VCF(self.vcf) if i.is_indel])))

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        print("\nNumber of SNVs: {}"
              .format(sum([1 for i in VCF(self.vcf) if i.is_snp])))
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        TOTO
        '''
        print("\nNumber of heterozygous variants: {}"
              .format(sum([1 for i in VCF(self.vcf) if i.num_het == 1])))
    
    def print_summary(self):
        print(__author__)
        self.get_average_quality_of_son()
        self.get_total_number_of_variants_of_son()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()

if __name__ == '__main__':
    print("Assignment 2")
    assignment1 = Assignment2()
    assignment1.print_summary()
    
    

