def avoids(word,forbidden):
    for i in range(len(forbidden)):
        if forbidden[i] in word:
            return True
        else:
            return False
word=raw_input("enter a word:")
forbidden=raw_input("enter forbidden letters as a string:")
if(avoids(word,forbidden)==False):
    print("does not contain")
else:
    print("contains")
            
