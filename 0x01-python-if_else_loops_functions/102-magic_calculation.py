#!/usr/bin/python3
# 102-magic_calculation.py
# Edgah Ogeto Gwaro <almasike000@gmail.com>


def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
