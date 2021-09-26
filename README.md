### DESCRIPTION

Tests of a binary search algorithm implementation.

### FEEDBACK

#### Issues:
1) `target == elements[index]` should be performed before modifying `low`/`high` variables, otherwise the result of `found = low <= high` is compromised.
2) missing type checks.
3) missing check if the list is empty.

#### Suggestions:
1) perform sorting of the list inside the function or add check if the list is sorted.
2) it is better to use `//` operator instead of converting `float` to `int`.
3) it is better to calculate the middle index as `low + (high - low) // 2` to avoid overflows.

### INSTALLATION

1. Install Python 3.x (https://www.python.org/downloads/)
2. Execute the following command from the project root directory to install all dependencies:
`pip3 install -U -r python_dependencies.txt`

### RUNNING

Execute the following command from the project root directory to run the tests:
`python3 -m pytest test_binary_search.py`
    
