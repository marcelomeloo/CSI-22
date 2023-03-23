def checkEmpty (list):
    for tuple in list:
        if len(tuple) == 0:
            list.remove(tuple)
    return list