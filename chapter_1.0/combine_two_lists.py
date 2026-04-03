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
    while i < len(list1) and j < len(list2):     # Loop until we reach the end of either list i or j, we will compare the current elements of both lists and append the smaller one to the result list, then move the pointer of that list forward.   
        if list1[i] < list2[j]:                 # if i < j then we append i to the list and move i forward, else we append j to the list and move j forward.
            list.append(list1[i])
            i += 1                              # Move the pointer of list1 forward
        else:
            list.append(list2[j])               # if j < i then we append j to the list and move j forward, else we append i to the list and move i forward.
            j += 1                              # Move the pointer of list2 forward     
    
    # Append any remaining elements from either list
    list.extend(list1[i:])
    list.extend(list2[j:])
    
    return list

print(combine_lists([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))