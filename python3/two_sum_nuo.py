# 1
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# You may assume that each input would have exactly one solution
# and you may not use the same element twice

# Solution 1 (nested for loops, O(N^2))

def two_sum(l, target):

    i = 0

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == target:
                return i, j
            else:
                j += 1
        i += 1

# Soulution 2 (dictionary, O(N))

def two_sum(l, target):

    d = {}
    for i in range(len(l)):
        if target - l[i] in d:
            return i, d[target - l[i]]
        else:
            d[l[i]] = i
