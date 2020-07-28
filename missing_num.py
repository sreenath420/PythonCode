def missing(list):
    return [x for x in range(list[0],list[-1]) if x not in list]


list=[1,4,5,7,10]

print(missing(list))

