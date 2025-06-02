def combine(items, k):
    solutions = []
    combine_rec(solutions, items, [], k)
    return solutions


def combine_rec(solutions, items, acc, k):
    if len(acc) == k:
        solutions.append(acc)
        return

    for i in range(len(items)):
        combine_rec(solutions, items[i + 1:], acc + [items[i]], k)


print(combine([1, 2, 3, 4, 5], 2))