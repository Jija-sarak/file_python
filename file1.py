my_file = open("people1-exercise.txt","w")
my_file.write("""rishabh - meerut
imtiyaz - delhi
nilima - cochin
rati - shimla
ayishah - delhi
raghu - shimla
naseer - kanpur
karthikeyan - delhi
salma - jaipur
pankaj - delhi
brijesh - delhi
govind - delhi
puneet - shimla
siddhi - delhi
suman - jaipur
rajeev - shimla
mohinder - delhi
rajendra - jaipur
priyanka - shimla
neela - delhi
sashi - jaipur
sarika - delhi
deepti - shimla
harshad - delhi
trishna - raipur
pradeep - jaipur
sekhar - delhi
nand - delhi
anoop - delhi
balwinder - tokyo""")
my_file.close()
my_file=open("people1-exercise.txt")
c=my_file.read()
my_file.close()
print(c)
