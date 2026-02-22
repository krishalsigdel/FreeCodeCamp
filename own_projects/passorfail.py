st_names=[]
passed=[]
failed=[]
#names and no of students
conti="y"
while conti.lower()=="y":
    no_st=int(input('enter no of students whose marks needs to be added.        :'))
    for x in range (1,no_st+1):
        inp=input(f'Enter name of student {x}       :')
        st_names.append(inp)
    conti=input("do you want to add more names?(y/n)        :")
#no of subjects
no_sub=int(input("Enter number of subjects      :"))
for st_name in st_names:
    flag=0
    marks=[]
    print (f'enter marks of "{st_name}"')
#to get marks in each subject
    for i in range (1,1+no_sub):
        mks_correct='y'
        while mks_correct=='y':
            inp_mks=int(input(f'Enter marks of subject {i} (#out of 100 )      :'))
            if inp_mks>100 or inp_mks<0:
                print('marks must be in between 0 and 100')   
            else:
                mks_correct="n"
                marks.append(inp_mks)
#to check if student passes in every subject
    for mark in marks:
        if mark >= 40:
            flag+=1
#check if student passed ot fail and store in corresponding list
    if flag==no_sub:
       passed.append(st_name)
    else:
       failed.append(st_name)

if len(passed)>0:
    print("name of passed students          :",passed)
if len (failed)>0:
    print("name of failed students          :",failed)