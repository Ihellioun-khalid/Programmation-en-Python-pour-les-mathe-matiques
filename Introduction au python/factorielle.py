#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank lin
and sume more text like here.

"""


def factorielle(n):
    """[description]: l'implementation de la fonction factorielle.

    @n: le number sur lequel on applique le factorielle
    n!=n*(n-1)*(n-2)....*1
    """
    if n > 0:
        return n * factorielle(n - 1)
    else:
        return 1
