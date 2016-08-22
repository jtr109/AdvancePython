# !/usr/bin/env python

example_list = [1, 2, 3, 4, 5, 6, 7, 8]
total = 20


def find_length(l):
    length = len(l)
    return length


def find_average(l):
    total = 10

    def find_total(l):
        return total

    return find_total(l) / find_length(l)

average = find_average(example_list)
length = find_length(example_list)
print("average = {}".format(average))
print("If total = 10: average = {}".format(10/length))
print("If total = 20: average = {}".format(20/length))