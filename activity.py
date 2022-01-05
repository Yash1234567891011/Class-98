def countWords():
    file=input("Enter the file name:")
    numberWords=0
    file1=open(file,"r")
    for line in file1:
        word=line.split()
        numberWords=numberWords+len(word)
    print("number of words in the file are ",numberWords)
countWords()        