lst = {}
orderedlst = []

while True:
    try:
        item = input("").upper()
        orderedlst.append(item)
        orderedlst.sort()
    except EOFError:
        for item in orderedlst:
            if item in lst:
                lst[item] += 1
            else:
                lst[item] = 1
        for i in lst:
            print(str(lst[i]), i)
        break
