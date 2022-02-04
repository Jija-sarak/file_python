banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
my_file1 = open("file-question3.txt","w")
for i in banks_list:
    my_file1.write(i)
    my_file1.write("\n")
my_file1.close()
my_file1 = open("file-question3.txt")
d = my_file1.read()
print(d)