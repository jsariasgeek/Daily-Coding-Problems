# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first 
# missing positive integer in linear time 
# and constant space. In other words, 
# find the lowest positive integer that
#  does not exist in the array. 
# The array can contain duplicates 
# and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

input_list = [3,4,-1,1]
input_list_2 = [1, 2, 0]


def check_positive_missing(input_list):
    max_number = max(input_list)
    min_number = min(input_list)
    new_list = [i for i in range(min_number, max_number) if i>0]
    for item in new_list:
        if item not in input_list:
            return item
    return max_number + 1

# print('Max: ', max(input_list))
# print('Min: ', min(input_list))

print(check_positive_missing(input_list_2))
