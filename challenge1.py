# Inputs: 
# arr: string of arbitrary length
# n (int): length of the subarrays
# Output:
# set of substrings of length n extracted from arr
def get_sub_strings(arr, n):
    sub_strings = set()
    len_str = len(arr)
    for i in range(0, len_str):
        if i + n > len_str:
            # Cannot build a substring of len n starting at position i
            return sub_strings
        sub_strings.add(arr[i:i+n])
    return sub_strings

# Input: 3 ordered strings of arbitrary length containing random capital letters
# Output: longest ordered string which all strings share
def longest_ordered_array(arr1, arr2, arr3):
    # Obtain the length of the shortest string
    min_length = min([len(arr) for arr in [arr1, arr2, arr3]])
    for i in range(min_length, 0, -1):
        set1 = get_sub_strings(arr1, i)
        set2 = get_sub_strings(arr2, i)
        set3 = get_sub_strings(arr3, i)
        common_sub_strings = set1 & set2 & set3
        if len(common_sub_strings) > 0:
            return common_sub_strings.pop()
        
    return ""

test1 = longest_ordered_array("UIBAZDBSIAHFB", "PQACIZDBIBDLAG", "QIDBCZDBKSHDVF")
assert test1 == "ZDB"

test2 = longest_ordered_array("ADDB", "CDDE", "EDDF")
assert test2 == "DD"

test3 = longest_ordered_array("UIBAZDBLSIAHFB", "PQACIZDBLIBDLAG", "QIDBCZDBLKSHDVF")
assert test3 == "ZDBL"

test4 = longest_ordered_array("ABCD", "EFGH", "IJK")
assert test4 == ""

test5 = longest_ordered_array("ABC", "CAR", "MAR")
assert test5 == "A"