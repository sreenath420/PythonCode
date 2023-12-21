def countVowels(words,vowels):
    #vowels='aeiouAEIOU'
    count = 0
    for i in range(len(words)):
        if words[i] in vowels:

            count +=1
    return count

words="I am America"
vowels='aeiouAEIOU'

print("count the vowels",countVowels(words,vowels))