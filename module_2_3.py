mylist = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(mylist):
    if mylist[i] >= 0:
        print (mylist[i])
    else:
        break
    i = i + 1