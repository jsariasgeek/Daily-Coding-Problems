# Good morning! Here's your coding interview problem for today.

# This problem was asked by Uber.

# Given an array of integers, return a new array such that each 
# element at index i of the new array is the product of all the 
# numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output 
# would be [2, 3, 6].

input = [1,2,3,4,5]
input_2 = [3,2,1]


def factorial(input_list):
    output_list = []
    for item in input_list:
        product = 1
        # multipliers_list = input_list.pop(input_list.index(item))
        multipliers_list = input_list.copy()
        multipliers_list.pop(input_list.index(item))
        for i in multipliers_list:
            product = product * i
        output_list.append(product)
    return output_list
        
        # print(input_list.index(item))
        # print(multipliers_list)
        

           
print(factorial(input_2))
