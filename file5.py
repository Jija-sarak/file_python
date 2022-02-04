a = open("number.txt","w")
a.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")
a.close()
n=open("number.txt","r")
sum = 0
for i in n:
    sum+=int(i)
print(sum)
