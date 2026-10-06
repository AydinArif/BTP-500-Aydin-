#
# Author: Aydin Arif
# Student Number: 170685234
#
# Place the code for your lab 2 here.  Read the specs carefully.
#
# To test, run the following command:
#     python3 lab2_tester.py
#

# Write the following 3 functions recursively

def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def linear_search(list, key):
    return linear_search_helper(list, key, 0)


def linear_search_helper(list, key, index):
    if index >= len(list):
        return -1
    if list[index] == key:
        return index
    return linear_search_helper(list, key, index + 1)


def binary_search(list, key):
    return binary_search_helper(list, key, 0, len(list) - 1)


def binary_search_helper(list, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if list[mid] == key:
        return mid
    if list[mid] < key:
        return binary_search_helper(list, key, mid + 1, high)
    return binary_search_helper(list, key, low, mid - 1)


