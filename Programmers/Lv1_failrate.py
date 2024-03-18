#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

fail = {} #dict
for i in range(1, N+1): # 1 2 3 4 5
    if i not in stages:
        fail[i] = 0
    else:
        fail[i] = stages.count(i) / len(stages)
        
        while i in stages:
            stages.remove(i)
ans = sorted(fail.items(), key = lambda x: x[1], reverse = True)
print([ans[i][0] for i in range(N)])