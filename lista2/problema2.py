def getMeanTuple (tuples):
    means = ()
    for tuple in tuples:
        means += (sumAll(tuple)/2,)
    return means

def sumAll (tuple):
    total = 0
    for num in tuple:
        total += num
    return total