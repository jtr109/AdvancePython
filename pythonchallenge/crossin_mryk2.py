def sort_and_unique(l):
    new_l = list(set(l))
    new_l.sort()
    return new_l

if __name__ == '__main__':
    l = [4, 7, 3, 4, 1, 9, 8, 3, 7]
    print(sort_and_unique(l))
