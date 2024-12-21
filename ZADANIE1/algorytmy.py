from ZADANIE1.tablica import MonitorowanaTablica

def insertion_sort(array: MonitorowanaTablica, left=0, right=None):
    if right is None:
        right = len(array) - 1

    i = left + 1
    while i <= right:
        j = i
        while j > left and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1

def bubble_sort(array: MonitorowanaTablica):
    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break

def shell_sort(array: MonitorowanaTablica):
    left = 0
    right = len(array) - 1

    h = 1
    while h <= (right - left) // 9:
        h = 3 * h + 1

    while h > 0:
        for i in range(left + h, right + 1):
            j = i

            item = array[i]
            while j >= left + h and item < array[j - h]:
                array[j] = array[j - h]
                j = j - h
            array[j] = item

        h = h // 3

def merge_sort(array: MonitorowanaTablica, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if left < right:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)

def merge(array: MonitorowanaTablica, left, mid, right):
    left_copy = array[left:mid + 1]
    right_copy = array[mid + 1:right + 1]

    left_idx, right_idx = 0, 0
    sorted_idx = left

    while left_idx < len(left_copy) and right_idx < len(right_copy):
        if left_copy[left_idx] <= right_copy[right_idx]:
            array[sorted_idx] = left_copy[left_idx]
            left_idx += 1
        else:
            array[sorted_idx] = right_copy[right_idx]
            right_idx += 1
        sorted_idx += 1

    while left_idx < len(left_copy):
        array[sorted_idx] = left_copy[left_idx]
        left_idx += 1
        sorted_idx += 1

    while right_idx < len(right_copy):
        array[sorted_idx] = right_copy[right_idx]
        right_idx += 1
        sorted_idx += 1


def quick_sort(array: MonitorowanaTablica, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if left < right:
        partition_idx = partition(array, left, right)
        quick_sort(array, left, partition_idx - 1)
        quick_sort(array, partition_idx + 1, right)

def partition(array: MonitorowanaTablica, left, right):
    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

def tim_sort(array: MonitorowanaTablica):
    MIN_RUN = 32

    def insertion_sort(array, left, right):
        for i in range(left + 1, right + 1):
            key_item = array[i]
            j = i - 1
            while j >= left and array[j] > key_item:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key_item

    def merge(array, left, mid, right):
        left_copy = array[left:mid + 1]
        right_copy = array[mid + 1:right + 1]

        left_idx, right_idx = 0, 0
        sorted_idx = left

        while left_idx < len(left_copy) and right_idx < len(right_copy):
            if left_copy[left_idx] <= right_copy[right_idx]:
                array[sorted_idx] = left_copy[left_idx]
                left_idx += 1
            else:
                array[sorted_idx] = right_copy[right_idx]
                right_idx += 1
            sorted_idx += 1

        while left_idx < len(left_copy):
            array[sorted_idx] = left_copy[left_idx]
            left_idx += 1
            sorted_idx += 1

        while right_idx < len(right_copy):
            array[sorted_idx] = right_copy[right_idx]
            right_idx += 1
            sorted_idx += 1

    n = len(array)

    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(array, start, end)

    size = MIN_RUN
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(left + size - 1, n - 1)
            right = min(left + size * 2 - 1, n - 1)
            if mid < right:
                merge(array, left, mid, right)
        size *= 2

algorytmy = [
    (insertion_sort, "Insertion Sort"),
    (bubble_sort, "Bubble Sort"),
    (shell_sort, "Shell Sort"),
    (merge_sort, "Merge Sort"),
    (quick_sort, "Quick Sort"),
    (tim_sort, "Tim Sort"),
]
