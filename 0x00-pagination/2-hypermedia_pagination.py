#!/usr/bin/env python3
"""Simple pagination
"""

import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int]:
    """Returns a tuple of size two containing a start index and
    an end index corresponding to the range of indexes
    """
    start = page_size * (page - 1)
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        if self.__dataset and page > len(self.__dataset):
            return []
        i = index_range(page, page_size)
        self.dataset()
        return self.__dataset[i[0]:i[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """Hypermedia pagination
        """
        data = self.get_page(page, page_size)
        next_page = None if len(
            data) == 0 or page * page_size >= len(self.__dataset) else page + 1
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": None if page == 1 else page - 1,
            "total_pages": math.ceil(len(self.__dataset) / page_size)
        }
