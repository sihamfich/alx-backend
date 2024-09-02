#!/usr/bin/env python3
"""
This module contains a simple helper function for calculating
the start and end indices for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing a start index and an end index corresponding
    to the range of indexes to return in a list for those particular
    pagination parameters.

    :param page: Current page number (1-indexed).
    :param page_size: Number of items per page.
    :return: Tuple (start_index, end_index) representing
            the start and end indices.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
