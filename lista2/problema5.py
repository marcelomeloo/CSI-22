# supose that we have: matrix = left * right
def multiplyMatrix (left, right):
    matrix = []
    for i in range(len(left)):
        line = []
        for j in range(len(right[0])):
            elem = sum(left[i][k]*right[k][j] for k in range(len(right)))
            line.append(elem)
        matrix.append(line)
    return matrix