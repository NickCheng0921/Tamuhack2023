# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:41:59 2023

@author: Nick Cheng
"""

class weightedListing:
    weight = 1e6
    url = ""
    title = ""
    def __init__(self, weight):
        self.weight = weight
    
    def __lt__(self, other):
        if self.weight < other.weight:
            return True
        else:
            return False

wl1 = weightedListing(weight = 10)
wl2 = weightedListing(weight = 0)
wl3 = weightedListing(weight = 100)
wl4 = weightedListing(weight = 17)

resultList = []

def sortedInsert(li, val):
    if li == []:
        li.append(val)
    else:
        for idx, ele in enumerate(li):
            if val < ele:
                li.insert(idx, val)
                return
        li.append(val)

'''
sortedInsert(resultList, wl1)
sortedInsert(resultList, wl2)
sortedInsert(resultList, wl3)
sortedInsert(resultList, wl4)

for x in resultList:
    print(x.weight)
'''
