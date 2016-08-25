def unqiue(listt):
    i = 1
    if listt == []:
        return True
    while (i < len(listt)):
        if listt[0] == listt[i]:
            return False
        else:
            i = i + 1
    else:
        return unqiue(listt[1:])


a = unqiue([1,2,3,6,4,5,6])
print a



