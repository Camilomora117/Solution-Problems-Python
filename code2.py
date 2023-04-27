
def sorted_array(array, s):
    """
    Function that takes in a non-empty array of integers sorted in ascending order
    :param array: Array of integers
    :param s: Range int
    :return: new array of the same length with the squares of the original integers also sorted in ascending order
    """
    response = []
    i_value_min = 0
    i_value_max = len(array) - 1

    for index in range(len(array)):

        value_min = array[i_value_min]
        value_max = array[i_value_max]

        if abs(value_min) >= abs(value_max):
            if value_min * value_min <= s * s:
                response.append(value_min * value_min)
            i_value_min += 1
        else:
            if value_max * value_max <= s * s:
                response.append(value_max * value_max)
            i_value_max -= 1

    return response[::-1]

def main():
    """
    Method main
    """
    array1 = [1, 2, 3, 5, 6, 8, 9, 10]
    array2 = [-2, -1]
    array3 = [-6, -5, 0, 5, 6]
    array4 = [-10, 10]
    s = 9
    print("s : " + str(9))
    print(str(array1) + " -> " + str(sorted_array(array1, s)))
    print(str(array2) + " -> " + str(sorted_array(array2, s)))
    print(str(array3) + " -> " + str(sorted_array(array3, s)))
    print(str(array4) + " -> " + str(sorted_array(array4, s)))

main()
