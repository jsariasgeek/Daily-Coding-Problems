# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, 
# return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] 
# and k of 17, return true since 10 + 7 is 17.

addends_list = [10, 15, 3, 8]
result = 17

def check_addends(addends_list, result):
    for item in addends_list:
        if addends_list.index(item)  == len(addends_list)-1:
            break
        new_addends_list = addends_list[addends_list.index(item):]
        for i in new_addends_list:
            if item + i == result:
                return True
    return False

print(check_addends(addends_list, result))
