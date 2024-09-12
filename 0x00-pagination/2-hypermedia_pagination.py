#!/usr/bin/env python3
"""simple pagination"""
import csv
import math

from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range of some page"""
    page -= 1
    return (page * page_size, page_size * (1 + page))


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """getting page using two variables"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        if end > len(data):
            end = -1
        if start > len(data):
            start = end

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """getting a dict info about the page"""
        data = self.get_page(page, page_size)

        start, end = index_range(page, page_size)
        next_page = page + 1 if end < len(self.__dataset) else None
        prev_page = page - 1 if start > 0 else None

        info = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": math.ceil(len(self.__dataset) / page_size),
        }

        return info
