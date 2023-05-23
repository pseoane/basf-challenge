
# Input: String containing an arbitrary number of r, b and g 
# ------------
# Output: Triplet of ints representing:
# triplet[0]: number of r
# triplet[1]: number of g
# triplet[2]: number of b
# ------------
# Example
# input: "rrgrb" -> (3, 1, 1)
def change_subset_representation(subset):
    return (subset.count("r"), subset.count("g"), subset.count("b"))

# Input: array containing an arbitrary number of r, g and b
# ------------
# Output: Maximum number of subsets in which the array can be split so that every subset
# contains equal color representations
def number_of_equal_colors(array):
    # Subsets whose length cannot be divided by 3 will never have an equal number of colors,
    # so in order to optimize the algorithm we iterate the array starting from 3 and with step 3
    for subset_length in range(3, len(array) + 1, 3):
        subsets = []
        for i in range(0, len(array), subset_length):
            subsets.append(change_subset_representation(array[i:i+subset_length]))
        
        # Check if all subsets have equal color representations. As subset_length starts
        # from the minimum possible subset length (3), once all subsets of subset_length
        # have equal color representations, it means that len(subsets) is the maximum
        # number of subsets into which the array can be divided
        if all(element[0] == element[1] and element[0] == element[2] for element in subsets):
            return len(subsets)
    return 0

assert number_of_equal_colors("rrbbgg") == 1
assert number_of_equal_colors("rbggbr") == 2
assert number_of_equal_colors("rrbbg") == 0
assert number_of_equal_colors("rbgrbgrbgrgb") == 4