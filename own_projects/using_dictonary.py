list_of_all=list([])
do_new="y"
while do_new=="y":
    print(f'1.input\n2.output\n3.append\n4.exit',)
    users_want=int(input('What do yo want to do (choose number from above)?     :'))

    if users_want==1:#checking if the user want to input data or not
        keys=input('enter the keys you want and seperate each key with comma","     :').split(",")#taking keys from user and spliting them to make a list of keys
        same_keys='y' 
        while same_keys=="y":
            reps=input('Enter how many data do you want to enter        :')#taking how many times the user want to enter data with same keys
            count=0
            while count<=int(reps):
                users_dict={}#creating empty dict to store the data of user and reset it for each new data entry.
                for key in keys:#looping through the keys to take values for each key from user and store it in dict
                    value=input(f'enter {key}       :')
                    users_dict[key]=value
                    count+=1
                print('append is taking place')
                list_of_all.append(users_dict)#appending the dict of user to the list of all data
            print('comming out of while loop')
            same_keys=input('do you want to enter more values with same keys? (y/n)      :').lower()    
            exit=input('enter any key to continue..........')
            # upto here is okay
    elif users_want==2:
        print('1. see all values')
        for index, key in enumerate(keys,2):
            print (f'{index}. search by {key}')
        out =int(input('enter what do you want as output(number)     :'))

        if out==1:
            for dicti in list_of_all:
                print(f'{dicti}')

        for index,key in enumerate(keys,2):#for finding what to search
            if out==index:
                s_key=key
                s_val=input(f'enter the {key} you want to search       :')
                for dicti in list_of_all:
                    for k,val in dicti.items():
                        if val==s_val and s_key==k:
                            print(dicti)
            exit=input('enter any key to continue..........')

    elif users_want==4:
        do_new="n"