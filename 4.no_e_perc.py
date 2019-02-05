list1=[]
list2=[]
def no_e(list1):
    for i in list1:
        if(('e' not in i)==True):
            list2.append(i)
            length1=len(list1)
            length2=len(list2)
    print("words not containing e:{}".format(list2))
    percentage=(float(length2)/float(length1))*100
    print("{}%".format(int(percentage)))

n=int(input("enter no of words:"))
for i in range(0,n):
    inp=raw_input("enter string:")
    list1.append(inp)
no_e(list1)
