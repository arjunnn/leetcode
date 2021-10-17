from typing import List, Union


def insertion_sort(array: List[Union[int, float]]) -> List[Union[int, float]]:
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array


print(insertion_sort([5.2, 4.10, 10.6, 1.453, 6.123, 2.89, 1.4, -1, -1.10, -1.1]))
