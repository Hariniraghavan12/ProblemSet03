from __future__ import print_function
def rotate_word(string,num):
    for ch in string:
        nc=ord(ch)
        nc1=nc+num
        ch1=chr(nc1)
        print(ch1,end="")
string=raw_input("enter a string:")
num=int(input("enter a number:"))
rotate_word(string,num)
