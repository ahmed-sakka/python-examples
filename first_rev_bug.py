import pdb

def findBug(rev):
    start = 0
    end = len(rev) - 1

    while (start <= end):

        mid = (start + end)/2
        print start, end, mid

        if rev[mid] == 'B':
            end = mid - 1
            if mid == start + 1:# or mid == start:
                return mid

        else:
            start = mid + 1

            if mid == end:
                return -1

print 1, ",", findBug(['G', 'B', 'B', 'B'])
print ['G', 'B', 'B', 'B'].index('B')
print 2, ",", findBug(['G', 'G', 'B', 'B'])
print 3, ",", findBug(['G', 'G', 'G', 'B'])
print 4, ",", findBug(['G', 'G', 'G', 'B', 'B'])
print 5, ",", findBug(['G', 'G', 'G', 'B', 'B', 'B'])
