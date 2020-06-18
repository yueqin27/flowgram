#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 
# @Author  : Yue Qin

'''
expected output when flowgram_cap = 0
{'A': 2, 'C': 1, 'T': 0, 'G': 3}
[1, 0, 1, 3, 0, 1, 0, 0, 1, 0, 1, 0, 2]

expected output when flowgram_cap = 2
{'A': 2, 'C': 1, 'T': 0, 'G': 3}
[1, 0, 1, 2, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0,2]

define idx as comp_strand's index, pre_idx as flow_order index;
both idx and pre_idx start from position 0; when there is a match, idx increases by 1, pre_cap increased by 1, stopped by there is a mismatch or cap reached, then pre_idx incresed by 1. 
'''

import os
import sys
import array
import numpy as np

def generate_flowgram(template_sequence="ATCCCGATAA", flow_order='TCAG', flowgram_cap = 0):
  base_pair = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
  upper_sequence = template_sequence.upper()
  comp_strand = [base_pair[i] for i in upper_sequence]
  order_dict = {}
  for i in range(len(flow_order)):
    order_dict[flow_order[i]] = i
  print(order_dict)
  pre_idx,pre_cap,idx = 0,0,0
  output_arr = []
  while idx < len(comp_strand):
    x = comp_strand[idx]
    index = order_dict[x]
    if pre_idx == index and flowgram_cap == 0 or pre_idx == index and pre_cap < flowgram_cap:
      pre_cap += 1
      if idx == len(comp_strand)-1:
        output_arr.append(pre_cap)
      idx += 1
    elif pre_idx == index and pre_cap >= flowgram_cap or pre_idx != index:
      output_arr.append(pre_cap)
      pre_cap = 0
      pre_idx += 1
      if pre_idx == 4:
        pre_idx = 0
  return output_arr

print(generate_flowgram(template_sequence="ATCCCGATAA", flow_order='TCAG', flowgram_cap = 2))
