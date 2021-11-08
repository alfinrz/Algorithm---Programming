# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:29:17 2021

@author: Intel
"""
from collections import Counter
s= 'I went to School today and I enjoyed it, school was pleasant'

count = Counter(s.lower().split())

for Hapax in count:
    if count[Hapax] == 1:
        print (Hapax)

