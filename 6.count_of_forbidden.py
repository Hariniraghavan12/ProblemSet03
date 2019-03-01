forb_list=[]
str2=''
list2=[]
count=0
def avoids(word,forb_list):
    for l in forb_list:
        if l not in word:
            list2.append(l)
            str2=''.join(list2)
            nl=str2.split()
    print(str2)
    print list2
    print len(nl)
word=raw_input("enter a word:")
forbidden=raw_input("enter a forbidden string:")
forb_list=forbidden.split(" ")
avoids(word,forbidden)
