import pytest

from binary_search import binary_search

even_size_list = [x for x in range(-5, 5)]
odd_size_list = [x for x in range(-5, 6)]
list_of_floats = [1.1, 2, 3.3, 4, 5.5, 6, 6.1, 6.2, 6.5]
not_sorted_list = [5, 0, 1, 3, 9, 11, 2, 8, 7, 4, 5]


def parametrize_test(elements):
    middle_element_index = (len(elements) - 1) // 2
    middle_element_even_index = middle_element_index if middle_element_index % 2 == 0 else middle_element_index + 1
    middle_element_odd_index = middle_element_even_index + 1
    missing_element_list = elements.copy()
    removed_el = missing_element_list.pop(middle_element_index)

    input_and_result_data = [
        (elements, elements[0], True),  # find first element
        (elements, elements[-1], True),  # find last element
        (elements, elements[middle_element_even_index], True),  # find element in the middle with even index
        (elements, elements[middle_element_odd_index], True),  # find element in the middle with odd index
        (elements, elements[len(elements) - 1] + 1, False),  # find last + 1 element
        (elements, elements[0] - 1, False),  # find first - 1 element
        (missing_element_list, removed_el, False)  # find missing element
    ]
    return pytest.mark.parametrize("elements,target,result", input_and_result_data,
                                   ids=[
                                       "find first element",
                                       "find last element",
                                       "find element in the middle with even index",
                                       "find element in the middle with odd index",
                                       "find last+1 element",
                                       "find first-1 element",
                                       "find missing element"
                                   ])


class TestBinarySearch:

    @parametrize_test(even_size_list)
    @pytest.mark.timeout(5)
    def test_even_size_list(self, elements, target, result):
        assert binary_search(elements, target) == result

    @parametrize_test(odd_size_list)
    @pytest.mark.timeout(5)
    def test_odd_size_list(self, elements, target, result):
        assert binary_search(elements, target) == result

    @parametrize_test(list_of_floats)
    @pytest.mark.timeout(5)
    def test_list_of_floats(self, elements, target, result):
        assert binary_search(elements, target) == result

    @parametrize_test(not_sorted_list)
    @pytest.mark.timeout(5)
    def test_not_sorted_list(self, elements, target, result):
        assert binary_search(elements, target) == result

    @pytest.mark.timeout(5)
    def test_list_of_same_elements(self):
        elements = [1, 1, 1, 1, 1, 1, 1, 1]
        assert binary_search(elements, 1) == True
        assert binary_search(elements, 0) == False

    @pytest.mark.timeout(5)
    def test_list_of_1_element(self):
        elements = [1]
        assert binary_search(elements, 1) == True
        assert binary_search(elements, 0) == False

    @pytest.mark.timeout(5)
    def test_empty_list(self):
        # TODO: clarify expected result: exception or False?
        elements = []
        assert binary_search(elements, 0) == False

    @pytest.mark.timeout(5)
    def test_list_of_strings(self):
        # TODO: clarify expected result: exception or False?
        elements = ["0", "1", "2"]
        assert binary_search(elements, 0) == False


if __name__ == '__main__':
    pytest.main([__file__, "-v"])
