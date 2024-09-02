# Simple Helper Function for Pagination

This project includes a Python module that provides a helper function named `index_range`. This function is designed to assist with pagination by calculating the start and end indices for a given page number and page size.

## Files
- `0-simple_helper_function.py`: Contains the `index_range` function.

## Usage
To use the `index_range` function, import it into your script and pass the desired page number and page size.

```python
from 0-simple_helper_function import index_range

result = index_range(2, 10)
print(result)  # Output: (10, 20)

