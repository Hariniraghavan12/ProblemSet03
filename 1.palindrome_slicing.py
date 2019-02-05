def is_palindrome(string):
    rev_string=string[::-1]
    if(rev_string==string):
        print("palindrome")
    else:
        print("not a palindrome")
string=raw_input("enter a string:")
is_palindrome(string)
