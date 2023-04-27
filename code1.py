
def switch_list(array, s):
    """
    If the input number contains a digit greater or equal than S, you will delete the digit from the
    number, for example with S=6, 61 becomes 1, and 6 will be deleted from the array
    """
    result = []
    for num in array:
        filtered_num = ''.join(n for n in str(num) if int(n) < s)
        if filtered_num != "":
            result.append(int(filtered_num))
    return result[::-1]

def main():
    """
    Method main
    """
    array1 = [1, 2, 3, 4, 5, 9]
    array2 = [10, 20, 30, 40]
    array3 = [9]
    array4 = [99]
    array5 = [95]
    array6 = [9, 2, 1]
    array7 = [90, 6, 5, 4, 3, 2, 7, 29, 1]
    s = 9
    print("s : " + str(9))
    print(str(array1) + " -> " + str(switch_list(array1, s)))
    print(str(array2) + " -> " + str(switch_list(array2, s)))
    print(str(array3) + " -> " + str(switch_list(array3, s)))
    print(str(array4) + " -> " + str(switch_list(array4, s)))
    print(str(array5) + " -> " + str(switch_list(array5, s)))
    print(str(array6) + " -> " + str(switch_list(array6, s)))
    print(str(array7) + " -> " + str(switch_list(array7, s)))


main()