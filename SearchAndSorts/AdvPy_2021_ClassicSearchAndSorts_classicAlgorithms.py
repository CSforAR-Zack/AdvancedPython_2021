# Classic Search and Sort Algorithms

# Searches: Linear Search and Binary Search

def linearSearch(values: list, target: int) -> int:
    """ Search a list and return the index if found.
    Returns -1 if target is not found.
    """

    for i in range(len(values)):
        if target == values[i]:
            return i
    
    return -1


def binarySearch(values: list, target: int) -> int:   
    """ Search a list and return the index if found.
    Returns -1 if target is not found.
    """

    lower: int = 0
    upper: int = len(values) - 1

    while lower <= upper:
        mid: int = (lower + upper) // 2

        if target == values[mid]:
            return mid
        elif values[mid] > target:
            upper = mid - 1
        else:
            lower = mid + 1

    return -1

# Sorts: Bubble, Merge, Selection, and Insertion

def bubbleSort(unsortedValues: list) -> None:
    """ Sorts a list of unsorted values. """

    done: bool = False
    sortedCount: int = 0

    while not done:
        done = True
        index: int = 0

        while index < len(unsortedValues) - 1 - sortedCount:
            if unsortedValues[index] > unsortedValues[index + 1]:
                swap(unsortedValues, index, index + 1)
                done = False
            index += 1
        sortedCount += 1

def insertion_sort(values: list) -> None:
    for i in range(1, len(values)):
        temp: int = values[i]
        j: int = i - 1
        while j >= 0 and values[j] > temp:
            values[j + 1] = values[j]
            j = j - 1
        values[j + 1] = temp
    
def selection_sort(values: list) -> None:
    for i in range(len(values)):
        best: int = i
        for j in range(i + 1, len(values)):
            if values[j] < values[best]:
                best = j
        swap(values, i, best)

def mergeSort(values: list) -> list:
    # Base Case: when the values is size 1 (sorted)
    if len(values) <= 1:
        return values

    # temp list that will hold our sorted values to return them later
    sortedValues: list = []

    # finding the mid so we can divide the list into lower and upper halves
    mid: int = len(values) // 2

    # Dividing the list in half and caling mergeSort again on each one
    # to further divide the list down into smaller halves
    # and then catching back the sorted smaller halves
    lowerHalf: list = mergeSort(values[:mid])
    upperHalf: list = mergeSort(values[mid:])

    # Sorting the halves that were returned from above
    # Checking the first item of each and the lower is inserted into
    # sortedValues first.
    while len(lowerHalf) > 0 and len(upperHalf) > 0:
        if lowerHalf[0] < upperHalf[0]:
            sortedValues.append(lowerHalf.pop(0))
        else:
            sortedValues.append(upperHalf.pop(0))

    # There might be some left over sorted values in each half
    # If there is, add them all (extend) to the end of sortedValues
    # since they must all be larger than what is already there.
    if len(lowerHalf) > 0:
        sortedValues.extend(lowerHalf)
    elif len(upperHalf) > 0:
        sortedValues.extend(upperHalf)   

    # Return the sorted values.
    return sortedValues     

# Helper Functions

def swap(values: list, i: int, j: int) -> None:
    """ Swap values[i] with values[j] inside of list values. """

    temp: int = values[i]
    values[i] = values[j]
    values[j] = temp