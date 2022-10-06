from typing import List
from random import choice, randint
import random
import time


ARRAY = [random.randint(13, 25) for _ in range(10**4)]


def buble_sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    offset = 1
    for _ in range(len(container)):
        for i in range(len(container) - offset):
            current_elem = container[i]
            next_elem = container[i+1]
            if current_elem > next_elem:
                container[i], container[i+1] = next_elem, current_elem
        offset += 1
    return container


def merge_func(sorted_left: List[int], sorted_right: List[int]):
    sorted_result = []
    current_left_index = 0
    current_right_index = 0

    while True:
        current_left_value = sorted_left[current_left_index]
        current_right_value = sorted_right[current_right_index]

        if current_left_value < current_right_value:
            sorted_result.append(current_left_value)
            current_left_index += 1
        else:
            sorted_result.append(current_right_value)
            current_right_index += 1

        if current_left_index == len(sorted_left):
            sorted_result.extend(sorted_right[current_right_index:])
            break
        if current_right_index == len(sorted_right):
            sorted_result.extend(sorted_left[current_left_index:])
            break

    return sorted_result


def merge_sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) == 1:
        return container

    middle_id = len(container) // 2

    left_part = merge_sort(container[:middle_id])
    right_part = merge_sort(container[middle_id:])

    return merge_func(left_part, right_part)


def quick_sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if not container:
        return container
    pivot = choice(container)
    return quick_sort([v for v in container if v < pivot])\
        + [v for v in container if v == pivot]\
        + quick_sort([v for v in container if v > pivot])


if __name__ == '__main__':
    start_time = time.time()
    buble_sort(ARRAY)
    print('\n', "--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    merge_sort(ARRAY)

    print('\n', "--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    quick_sort(ARRAY)
    print('\n', "--- %s seconds ---" % (time.time() - start_time))
