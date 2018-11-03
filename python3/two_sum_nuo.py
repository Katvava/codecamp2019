# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# You may assume that each input would have exactly one solution
# and you may not use the same element twice

def two_sum(l, target):

    i = 0

    if len(l) < 2:
        print('invalid input')
    elif len(l) == 2:
        return 0, 1
    else:
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] == target:
                    return i, j
                else:
                    j += 1
            i += 1
