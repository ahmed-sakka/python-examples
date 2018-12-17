def avg(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    avg = float(sum)/len(args)
    return avg

print avg(1,3)
print avg(1,3,6)
