from classicAlgorithms import linearSearch, binarySearch, bubbleSort, mergeSort
def main():
    values: list = [0, 2, 4, 7, 9, 23, 24, 36, 60, 62]
    target: int = 36

    # print(f'{target} is at index {linearSearch(values, target)}.')
    # print(f'{target} is at index {binarySearch(values, target)}.')

    unsortedValues: list = [7, 23, 3, 24, 62, 9, 36, 60, 4, 0]
    # bubbleSort(unsortedValues)
    # print(unsortedValues)

    sortedList: list = mergeSort(unsortedValues)
    print(sortedList)

main()