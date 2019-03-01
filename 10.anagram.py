def is_anagram(string1,string2):
    str1_list=list(string1)
    str2_list=list(string2)
    str1_list.sort()
    str2_list.sort()
    if(str1_list==str2_list):
        return True
    else:
        return False
string1=raw_input("enter the first string:")
string2=raw_input("enter the second string:")
is_anagram(string1,string2)
    
