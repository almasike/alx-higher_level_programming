#!/usr/bin/python3
# 7-islower.py
# Edgah o Gwaro


def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
