def removeEmpty (list):
    cleanList = list[:]
    for tuple in cleanList:
        if len(tuple) == 0:
            cleanList.remove(tuple)
    return cleanList
