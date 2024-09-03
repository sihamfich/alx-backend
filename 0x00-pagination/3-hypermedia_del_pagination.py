#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server class with no
        dataset and no indexed dataset."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset,
        loading it from the CSV file if necessary."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by position, starting from 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Retrieve a page of data starting
        from a given index, with a given page size.

        Args:
            index (int): The start index of the page.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing:
                - 'index': the starting index of the page.
                - 'data': a list of items in the page.
                - 'page_size': the number of items per page.
                - 'next_index': the index of the first
                item after the current page.
        """
        # Assertions to ensure valid index and page size
        assert isinstance(index, int) and index >= 0, \
            "Index must be a non-negative integer."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer."

        dataset = self.indexed_dataset()  # Get the indexed dataset
        data = []  # Initialize an empty list to hold the page data
        current_index = index  # Start with the given index

        # Collect items for the requested page size
        while len(data) < page_size and current_index in dataset:
            data.append(dataset[current_index])
            current_index += 1

        # Determine the next index to query
        next_index = current_index

        # Return the dictionary with page information
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
