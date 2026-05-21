#!/usr/bin/env python3
"""
This module writes a type-annotated function sum_mixed_list which takes 
a list mxd_lst of integers and floats and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats."""
    return sum(input_list)
