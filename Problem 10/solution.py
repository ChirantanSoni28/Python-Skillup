def sum_no_duplicates(l):
    x = []
    for n in l:
        if l.count(n) == 1:
            x.append(n)
    return sum(x)
