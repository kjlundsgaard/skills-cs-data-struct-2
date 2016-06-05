#Sorting


def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    # go through list as many times as there are items in list so you go back and check every item
    for i in range(len(lst)):
        # set swap to False where a swap has not yet been made, will change when swap is made
        swap = False
        # go through list until the last item
        for j in range(len(lst) - 1):
            # swap position if one is higher
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
        # if no swap has happened, it's already sorted, so we don't need to revisit
        if not swap:
            break

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    # go through lists, compare list1[0] to list2[0] and pop item from whichever is less, put in new list
    new_list = []
    while len(list1) != 0 or len(list2) != 0:
        if not list1:
            new_list.append(list2.pop(0))

        elif not list2:
            new_list.append(list1.pop(0))

        elif list1[0] < list2[0]:
            new_list.append(list1.pop(0))

        else:
            new_list.append(list2.pop(0))

    return new_list

##########ADVANCED##########


def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(lst) == 1:
        return lst

    mid = len(lst) / 2

    list1 = merge_sort(lst[:mid])
    list2 = merge_sort(lst[mid:])

    new_list = []
    while len(list1) != 0 or len(list2) != 0:
        if not list1:
            new_list.append(list2.pop(0))

        elif not list2:
            new_list.append(list1.pop(0))

        elif list1[0] < list2[0]:
            new_list.append(list1.pop(0))

        else:
            new_list.append(list2.pop(0))

    return new_list

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print