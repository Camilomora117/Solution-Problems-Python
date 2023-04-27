
def last_change(array):
    """
    Problem Non-constructible change
    :param array: Array of integers
    :return: Integer that represents the minimum amount of change
    """
    array.sort()
    change = 0
    for coin in array:
        if coin > change + 1:
            break
        change += coin
    return change + 1

def main():
    """
    Method main
    """
    array1 = [5, 7, 1, 1, 2, 3, 22]
    array2 = [1, 1, 1, 1, 1]
    array3 = [1, 5, 1, 1, 1, 10, 15, 20, 100]

    print(last_change(array1))
    print(last_change(array2))
    print(last_change(array3))

main()