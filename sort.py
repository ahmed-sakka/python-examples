L = [4, 6, 3, 1]
def compare(a, b):
        return cmp(int(a), int(b)) # compare as integers

L.sort(compare)
print L

L = [[4, 2], [6, 1], [3, 1], [1, 3], [1, 1]]
def compare_columns(a, b):
        # sort on ascending index 0, descending index 1
        return cmp(a[0], b[0]) or cmp(b[1], a[1])

out = sorted(L, compare_columns)
print out
