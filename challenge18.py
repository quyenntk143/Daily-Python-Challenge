lst = list()
while True:
       inp = input("enter a number: ")
       number = int(inp)
       if inp == '0':break
       lst.append(number)
lst.sort()
for i in lst:
    print(i)
