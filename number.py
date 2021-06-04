def countWordsfromfile():
    fileName=input("Enter The FIle Name:")
    numberofWords=0
    file=open(fileName,"r")
    for line in file:
        words=line.split()
        numberofWords=numberofWords+len(words)
    print("Number Of Words:")
    print(numberofWords)

countWordsfromfile()