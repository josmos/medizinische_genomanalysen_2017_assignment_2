#! /usr/bin/env python3

import vcf
import numpy as np
import os

__author__ = 'Josef Moser'


class Assignment2:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        self.vcf = vcf.Reader(filename="AmpliseqExome.20141120.NA24385.vcf")
        self.records = list([i for i in self.vcf])

    def get_average_quality_of_son(self):
        '''
        Get the average PHRED quality of all variants
        :return: 
        '''
        s = np.mean([i.QUAL for i in self.records])
        print("Average PHRED Score is {}".format(s))

    def get_total_number_of_variants_of_son(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        sum = len(self.records)
        print("Number of Variants {}".format(sum))
    
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        source = "##source="
        var_caller = [h.lstrip(source) for h in self.vcf._header_lines
                      if h.startswith(source)][0]
        print("Variant Caller: {}".format(var_caller.strip('"')))

    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        ref = "##reference="
        path = [h.lstrip(ref) for h in self.vcf._header_lines
                if h.startswith(ref)][0]
        version = os.path.basename(path).strip(".fasta")
        print("Reference Version: {}".format(version))
        
    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs 
        :return: 
        '''
        indel_cnt = len([i for i in self.records if i.is_indel])
        print("Number of indels: {}".format(indel_cnt))

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        snp_cnt = len([i for i in self.records if i.is_snp])
        print("Number of SNVs: {}".format(snp_cnt))
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        TOTO
        '''

        
    
    def print_summary(self):
        # self.get_average_quality_of_son()
        # self.get_total_number_of_variants_of_son()
        # self.get_variant_caller_of_vcf()
        # self.get_human_reference_version()
        # self.get_number_of_indels()
        # self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()

        
if __name__ == '__main__':
    print("Assignment 2")
    assignment1 = Assignment2()
    assignment1.print_summary()
    
    

