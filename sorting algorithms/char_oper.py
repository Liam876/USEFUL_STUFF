# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 16:21:36 2021

@author: Admin
"""

def ch_instr (ch,st):
    count = 0
    for c in st:
        if c == ch:
            count+= 1
    return count

def non_rep(st):
    if len(st) == 1:
        return st
    i = 0
    while(i < len(st)):
        if (st[i] == st[i+ 1]):
            while (i != len(st) - 1 and  st[i] == st[i+ 1]):
                i = i + 1
            i = i + 1
            if (i == len (st)-1 and st[i] != st[i -1]):
                return st[i]
        else:
            return st[i]
    return 'no char'




