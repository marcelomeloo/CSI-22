# supose that we have: matrix = left * right
def multiplyMatrix (left, right):
    matrix = []
    for i in range(len(left)):
        line = []
        for j in range(len(right[0])):
            entries = []
            for k in range(len(right)):
                entries.append(left[i][k]*right[k][j])
            line.append(sum(entries))
        matrix.append(line)
    return matrix
