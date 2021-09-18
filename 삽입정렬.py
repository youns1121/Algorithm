def insertion_sort(num):
    for a in range(1, len(num)):
        for b in range(a, 0, -1):
            if num[b] < num[b-1]:
                   num[b], num[b-1] = num[b-1], num[b]

    return num

num = [5, 4, 6, 1, 2, 3]
print(insertion_sort(num))



