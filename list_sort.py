n = int(input("enter:"))
l=[]
for x in range(n):
    i = int(input())
    l.append(i)
    l.sort()
if 4 in l:
    l.remove(4)
    print(l[-1])
    
