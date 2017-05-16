def find_minimum(arr):
    result = arr[0]

    for el in arr:
        if el < result:
            result = el

    return result


def selection_sort(arr):
    result = []

    for _ in range(len(arr)):
        minimum = find_minimum(arr)
        result.append(minimum)
        arr.remove(minimum)

    return result
