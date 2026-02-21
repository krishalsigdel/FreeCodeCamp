st_names=[]
passed=[]
failed=[]
conti="y"
while conti.lower()=="y":
    inp=input("Enter students name      :")
    st_names.append(inp)
    conti=input("do you want to add more names?(y/n)")

no_sub=input("Enter number of subjects")
for st_name in st_names:
    marks=[]
    print (f'enter marks of{st_name}')
    for i in range (int(no_sub)):
        inp_mks=int(input(f'Enter marks of subject {i}      :'))
        marks.append(inp_mks)

    totalmarks=sum(marks)
    percent=int(totalmarks/int(no_sub))
    if percent >= 40:
       passed.append(st_name)
    else:
       failed.append(st_name)
print("name of passed students          :",passed)
print("name of failed students          :",failed)