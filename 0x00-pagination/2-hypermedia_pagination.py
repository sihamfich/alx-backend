#!/usr/bin/env python3
"""
Server class to paginate a database of popular
baby names with hypermedia pagination.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing a start index and an end index corresponding
    to the range of indexes to return in a list for those particular
    pagination parameters.

    :param page: Current page number (1-indexed).
    :param page_size: Number of items per page.
    :return: Tuple (start_index, end_index)
            representing the start and end indices.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


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
        """
        Get a page of the dataset.

        :param page: Current page number (1-indexed).
        :param page_size: Number of items per page.
        :return: A list of rows corresponding to the page of the dataset.
        """
        # Validate the inputs
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        # Get the dataset
        dataset = self.dataset()

        # Calculate the start and end indices
        start_index, end_index = index_range(page, page_size)

        # Return the appropriate slice of the dataset
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page of the dataset along with hypermedia information.

        :param page: Current page number (1-indexed).
        :param page_size: Number of items per page.
        :return: A dictionary containing hypermedia information.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
