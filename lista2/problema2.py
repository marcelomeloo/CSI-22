def getMeanTuple (tuples):
    means = ()
    for tuple in tuples:
        means += (sum(tuple)/2,)
    return means
