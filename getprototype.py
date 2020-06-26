def getprototype(row, prototypeneeded, root, element):
    for column in row:
        if column is not None:
            prototypeneeded = False
        else:
            prototypeneeded = True
            break
    if not prototypeneeded:
        root.append(element)
    return prototypeneeded, root