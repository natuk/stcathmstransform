def getprototype(row, prototypeneeded, root, element):
    for column in row:
        if column is not None:
            root.append(element)
            prototypeneeded = False
        else:
            prototypeneeded = True
            break
    return prototypeneeded, root