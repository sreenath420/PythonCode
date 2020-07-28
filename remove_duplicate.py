def remove(duplicate):
    single_list=[]
    for n in duplicate:
        if n not in single_list:
            single_list.append(n)

    return single_list


duplicate = [12,11,12,14,12,13,20,19,4,5,4,3,6,9]

print(remove(sorted(duplicate)))