# Write a function to combine two lists
# Write a function named combine_lists that accepts two lists of integers as parameters. 
# Consider that the two lists are already sorted (The numbers are already in order from smallest to biggest number). 
# Your function should return a list that combines the two lists and at the same time is itself also sorted. 
# To be clear all elements of the input lists should be in the output list and len(input_list1)+len(input_list2) == len(output_list). 
# Notice that your function should return the list, not print it.


def combine_lists(list1, list2):
    
    i = 0
    j = 0
    list = []
    
    # Merge the two lists while maintaining sorted order
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list.append(list1[i])
            i += 1
        else:
            list.append(list2[j])
            j += 1
    
    # Append any remaining elements from either list
    list.extend(list1[i:])
    list.extend(list2[j:])
    
    return list

print(combine_lists([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))