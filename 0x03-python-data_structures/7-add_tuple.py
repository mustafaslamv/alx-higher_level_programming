#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    b1, b2 = (0, 0) if len(tuple_b) < 2 else tuple_b[:2]
    return (a1 + b1, a2 + b2)
