def abecedarian(word):
    flag=0
    for i in range(len(word)-1):
        if(word[i]>word[i+1]):
            flag=1
            break
    if(flag==1):
        return False
    else:
        return True

word=raw_input("enter a word:")
print(abecedarian(word))
