#!/usr/bin/env python3

import csv
import math
from typing import List


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
        try:
            assert page > 0 and page_size > 0, "raised with negative values"
            assert isinstance(page, int) and isinstance(
                page_size, int
            ), "raised when page and/or page_size are not ints"
        except AssertionError as err:
            print("AssertionError ", err)

        page -= 1
        start = page * page_size
        end = start + page_size

        # end is passing the end of csv
        if end > len(self.__dataset):
            end = -1
        # start is passing the csv file
        if start > len(self.__dataset):
            return []
        return self.__dataset[start : end + 1]
