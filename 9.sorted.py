def is_sorted(str_list):
    flag=0
    for i in range(len(str_list)-1):
        if(str_list[i]>str_list[i+1]):
            flag=1
            break
    if(flag==1):
        return False
    else:
        return True

string=raw_input("enter a string:")
str_list=list(string)
print(is_sorted(str_list))
    
