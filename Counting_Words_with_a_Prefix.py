words=["bilingual", "macroeconomics", "enlarge", "macroscopic", "monolingual"]
prefix="macro"
counter=0
for i in range(len(words)):
    prefix_count=words[i][:len(prefix)]
    if prefix_count==prefix:
        counter +=1
print("print the prefixing word:",counter)

#output:-
print the prefix word: 2
