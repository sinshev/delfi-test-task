def binary_search(elements, target):
    """
    returns True if the target is in the list, and False if not
    -elements is a sorted list
    -target is a value to be searched
    """
    low = 0
    high = len(elements) - 1

    while True:
        index = int((low + high) / 2)
        if target < elements[index]:
            high = index - 1
        else:
            low = index + 1
        if low > high or target == elements[index]:
            break
    found = low <= high
    return found
