def sumList(matrix):
    return list(map(sumLine, matrix))

def sumLine(line):
    total = 0
    for elem in line:
        total += elem
    return total