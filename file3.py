my_file2 = open("question3.txt","w")
my_file2.write("""rishabh - meerut
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
my_file2.close()
a = open("question3.txt","r")
for i in a:
    if "delhi" in i:
        p= open("delhi.txt","a")
        p.write(i)
    elif "shimla" in i:
        s = open("shimla.txt","a")
        s.write(i)
    else:
        t = open("others.txt","a")
        t.write(i)
a.close()