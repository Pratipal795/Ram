students=[{'name': {'name': 'Ram', 'roll': {'roll': 101}, 'father_name': 'Dashrath', 'school_or_clg': 'MIT', 'class_name': 'BE'}},
          {'name': {'name': 'Sita', 'roll': {'roll': 102}, 'father_name': 'janak', 'school_or_clg': 'SAGE', 'class_name': 'BE'}},
          {'name': {'name': 'Pratik', 'roll': {'roll': 103}, 'father_name': 'Makhan', 'school_or_clg': 'MIT', 'class_name': 'BE'}},
          {'name': {'name': 'Sakshi', 'roll': {'roll': 104}, 'father_name': 'Surendra', 'school_or_clg': 'SVVC', 'class_name': 'ME'}}]

mark=[{'name': {'name': 'Ram', 'roll': {'roll': 101}, 'marks': {'maths': 23, 'phy': 45, 'che': 65, 'hin': 23, 'eng': 67}}},
      {'name': {'name': 'Sita', 'roll': {'roll': 102}, 'marks': {'maths': 23, 'phy': 43, 'che': 45, 'hin': 65, 'eng': 78}}},
      {'name': {'name': 'Pratik', 'roll': {'roll': 103}, 'marks': {'maths': 34, 'phy': 54, 'che': 78, 'hin': 98, 'eng': 34}}},
      {'name': {'name': 'Sakshi', 'roll': {'roll': 104}, 'marks': {'maths': 22, 'phy': 33, 'che': 44, 'hin': 2, 'eng': 87}}}]

def show():
    for i in range(1,60):
        print("-",end="")
def per():
    if s>33:
        print(f"\t\t!!hurray you are passed with {s}%!!")
    else:
        print(f"\t\tSorry you are Fail with {s}%%")
while True:
    data=int(input("""Press 1 for Add student detail
                     \n Press 2 For Add marks
                     \n Press 3 For get student result 
                     \n Press 4 for delete student record
                     \n Press 5 for check perticular clg list
                     \n Press 6 for exit from the project """))
    try:
        data= int(data)
    except:
        print("You enter Wrong value")
        continue
    if data == 1:
        a=int(input("how many student you want to add"))
        for i in range(a):
            name=input("enter student name")
            n=name.capitalize()
            roll_number=int(input("enter student roll number"))
            c=0
            for k in students:
                if k['name']['roll']['roll']==roll_number:
                    c+=1
                    print("roll number already registered")
                    break
            if c==0:
                father_name=input("enter student father's name")
                f=father_name.capitalize()
                school_or_clg=input("enter student school or clg name")
                s=school_or_clg.upper()
                class_name=input("enter student class name")
                c=class_name.upper()
                print()
                student = {'name': {'name':n,  
                            'roll':{'roll':roll_number},            
                            'father_name':f, 'school_or_clg':s, 'class_name':c}}
                students.append(student)
        print(students)
        break
    elif data==2:
        r=int(input("enter your roll number here"))
        check=0
        for student in students:
            if student['name']['roll']['roll']==r:
                check+=1
                print("you are welcome")
                try:
                    m=int(input("enter maths marks"))
                    if m>101:
                        print(f"your entered number is {m} plz enter number between 1 to 101")
                        break
                    p=int(input("enter physics marks"))
                    if p>101:
                        print(f"your entered number is {p} plz enter number between 1 to 101")
                        break
                    c=int(input("enter chemistry marks"))
                    if c>101:
                        print(f"your entered number is {c} plz enter number between 1 to 101")
                        break
                    h=int(input("enter hindi marks"))
                    if h>101:
                        print(f"your entered number is {h} plz enter number between 1 to 101")
                        break
                    e=int(input("enter english marks"))
                    if e>101:
                        print(f"your entered number is {e} plz enter number between 1 to 101")
                        break
                except ValueError:
                    print("plz enter only digits")
                    continue
                #marks={'name': {'name':student['name']['name'],  
                         #'roll':{'roll':r,'marks':{'maths':m, 'phy': p, 'che': c, 'hin':h, 'eng':e}},            
                        #}}



                marks={'name': {'name': student['name']['name'], 'roll': {'roll':r}, 'marks': {'maths':m,"phy":p,"che":c,"hin":h,"eng":e}}}     
                mark.append(marks)
                print(mark)
                break
        if check==0:
            print("roll number not registered")
    elif data == 3:
        a=int(input("enter your roll number here"))
        for i in mark:
            if i['name']['roll']['roll']==a:
                show()
                print()
                print("\t\tGovernment Higher Secondary School,Hatod")
                show()
                print()
                print("Subject-Code",end=" ")    
                print(" Subject",end="  ")
                print("Max Marks",end="  ")
                print("Obtained-Marks",end="  ")
                print("Total")
                print("   001","\t\tMaths\t" "100","\t   ",i['name']['marks']['maths'],"\t\t","  ",i['name']['marks']['maths'])
                print("   002","\t\tPhysics\t" "100","\t   ",i['name']['marks']['phy'],"\t\t","  ",i['name']['marks']['phy'])
                print("   003","\t\tChemis\t" "100","\t   ",i['name']['marks']['che'],"\t\t","  ",i['name']['marks']['che'])
                print("   004","\t\tHindi\t" "100","\t   ",i['name']['marks']['hin'],"\t\t","  ",i['name']['marks']['hin'])
                print("   005","\t\tEnglish\t" "100","\t   ",i['name']['marks']['eng'],"\t\t","  ",i['name']['marks']['eng'])
                show()
                print()
                n=i['name']['marks']['maths']+i['name']['marks']['phy']+i['name']['marks']['che']+i['name']['marks']['hin']+i['name']['marks']['eng']
                print("\t\t","\tM_To=500","  ","Obt=",n,"\tTotal=",n)
                show()
                print()
                s=n/5
                per()   
                print()
                print()
                print()
            
                break
        else:
            print("invalid roll no")
            break
    elif data == 4:
        a=input("enter your name")
        aa=a.capitalize()
        b=int(input("enter your roll number"))
        check=0
        for a1 in students:
            if a1['name']['name']==aa and a1['name']['roll']['roll']==b:
                check+=1
                del a1['name']
                for b1 in mark:
                    if b1['name']['name']==aa and b1['name']['roll']['roll']==b:
                        del b1['name']
                print(students)
                print()
                print()
                print(mark)
                break
        if check==0:
            print("student not found")
            break
    elif data==5:
        n=input("enter you clg name here")
        up=n.upper()
        check=0
        for i in students:
            if i['name']['school_or_clg']==up:
                print(i['name'])
        break

    elif data == 6:
        print("exit ho gae ho aap ")
        break
        
        
                
