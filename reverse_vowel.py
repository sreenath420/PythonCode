def reverseVowel(s):
    vowels='aeiouAEIOU'
    s=list(s)
    i,j=0,len(s)-1

    print(j)
    while i < j:
        if s[i] not in vowels:
            #print('i value',s[i])
            i +=1
        elif s[j] not in vowels:
            print('j value',s[j])
            j -=1
        else:
            s[i],s[j]=s[j],s[i]
            i +=1
            j -=1
    return ''.join(s)
s='ujjwalae'

print(reverseVowel(s))