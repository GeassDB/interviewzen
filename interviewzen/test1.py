#!/usr/bin/env python3

def even_divided_by_two(l):
    res = []
    for num in l:
        if not num % 2:
            res.append(num/2)
    return res
