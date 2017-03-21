#! /usr/bin/env python3

import vcf
import numpy as np
import os
import subprocess

__author__ = 'Josef Moser'


class Assignment2:
    
    def __init__(self):
        if not os.path.isfile("AmpliseqExome.20141120.NA24385.vcf"):
            subprocess.call(["wget", "ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/data/"
                                     "AshkenazimTrio/analysis/IonTorrent_TVC_03162015/"
                                     "AmpliseqExome.20141120.NA24385.vcf"])
        self.vcf = vcf.Reader(filename="AmpliseqExome.20141120.NA24385.vcf")
        self.header = self.vcf._header_lines
        self.records = list([i for i in self.vcf])

    def get_average_quality_of_son(self):
        '''
        Get the average PHRED quality of all variants
        :return: 
        '''
        s = np.mean([i.QUAL for i in self.records])
        print("\nAverage PHRED Score is {}".format(s))

    def get_total_number_of_variants_of_son(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        sum = len(self.records)
        print("\nNumber of Variants {}".format(sum))

    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        var_caller = [h.lstrip("##source=") for h in self.header if h.startswith("##source=")][0]
        print("\nVariant Caller: {}".format(var_caller.strip('"')))

    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        path = [h.lstrip("##reference=") for h in self.header if h.startswith("##reference=")][0]
        version = os.path.basename(path).strip(".fasta")
        print("\nReference Version: {}".format(version))
        
    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs 
        :return: 
        '''
        indel_cnt = len([i for i in self.records if i.is_indel])
        print("\nNumber of indels: {}".format(indel_cnt))

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        snp_cnt = len([i for i in self.records if i.is_snp])
        print("\nNumber of SNVs: {}".format(snp_cnt))
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        TOTO
        '''
        het = [i for i in self.records if i.num_het == 1]
        print("\nNumber of heterozygous variants: {}".format(len(het)))
    
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
    
    

