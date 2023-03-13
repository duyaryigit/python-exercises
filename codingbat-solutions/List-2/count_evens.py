'''

Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
'''


def count_evens(nums):
    count = 0
    for i in range(0, len(nums), 1):
        if nums[i] % 2 == 0:
            count += 1
    return count
