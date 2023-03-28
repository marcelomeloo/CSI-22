def bigContainsSmall (bigStr, smallStr):
    for smallChar in smallStr:
        if bigStr.find(smallChar) < 0:
            return False
    return True