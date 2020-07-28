# [10,20,30,40,50,40,40,60,70]
#Range(40-70)=>[40,50,40,40,60,70]=> no.of elements


def count(num,h,l):
    c =0
    for x in num:
        if x>=h and x<=l:
            c +=1
    return c

num=[10,20,30,40,50,40,40,60,70]
h=30
l=70
print("number of elements",count(num,h,l))