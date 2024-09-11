#!/usr/bin/env python3
"""simple helper on pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    if page == 1:
        page = 0
    """index range of some page"""
    return (page * page_size, page_size * (1 + page))
