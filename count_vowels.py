#count the number of vowels in given string
input="i am going to OffIce"
vowel="aeiouAEIOU"
count = 0
print(len(input))
for i in range(len(input)):
    if input[i] in vowel:
        count +=1
print(count)


