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
    total_mks=input(f'Enter total marks of each subject (this should be same for all subjects)        :')
    for i in range (1,1+no_sub):
        mks_correct='y' 
        while mks_correct=='y':#to input mks again if user input marks is not in between 0-100
            inp_mks=int(input(f'Enter marks of subject {i} (#out of {total_mks} )      :'))
            if inp_mks>int(total_mks) or inp_mks<0:        #check if mks is betwn 0-total marks(upto line 27)
                print(f'marks must be in between 0 and {total_mks}')   
            else:
                mks_correct="n"#exit while loop,hence increase the value of i
                marks.append(inp_mks)
#to check if student passes in every subject
    for mark in marks:
        if mark >= 40/100*int(total_mks): #check if marks is greater than or equal to 40% of total marks
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