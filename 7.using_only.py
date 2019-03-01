flag=0
def using_only(word,list_str):
    for i in word:
        if i in list_str:
            flag=1
        else:
            flag=0
            break
    if flag==1:
        return True
    else:
        return False
word_str=raw_input("enter a word:")
word_str.lower()
word_list=word_str.split(' ')
word=''.join(word_list)
#print word
string=raw_input("enter a string:")
string.lower()
list_str=list(string)
print(using_only(word,list_str))
    
