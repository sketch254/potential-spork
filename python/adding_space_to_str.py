def addSpace(str, spaces):
    i, j = 0, 0 
    res = []

    while i < len(str) and j < len(spaces):
        if i < spaces[j]:
            res.append(str[i])
            i += 1
        else:
            res.append(" ")
            j +=1

    if i < len(str):
        res.append(str[i:])

    return "".join(res)


print(addSpace("helloworld",[5]))
