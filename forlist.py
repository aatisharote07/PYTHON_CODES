datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in range(len(datalist)):
    x=type(datalist[i]) 
    print(f"{datalist[i]}-{x}")
    