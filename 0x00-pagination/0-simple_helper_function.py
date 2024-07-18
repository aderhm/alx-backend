#!/usr/bin/env python3
""" Simple helper function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """ Returns a tuple of size two containing a start index and
    an end index corresponding to the range of indexes
    """
    start = page_size * (page - 1)
    end = start + page_size
    return (start, end)
