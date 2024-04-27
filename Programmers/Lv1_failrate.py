#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

fail = {} #dict
giri = len(stages) # 8
for i in range(1, N+1): # 1 2 3 4 5
    cnt = stages.count(i)
    if cnt == 0:
        fail[i] = 0
    else:
        fail[i] = cnt/ giri
        giri -= cnt
ans1 = sorted(fail, key= lambda x: fail[x], reverse=True)

ans2 = sorted(fail.items(), key= lambda x: x[1], reverse=True)
print([ans2[i][0] for i in range(N)])

