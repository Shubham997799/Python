rollno=int(input("Enter The Roll Number"))
name=input("Enter The Name")
sci=int(input("Enter The Marks Of Science"))
maths=int(input("Enter The Marks Of Maths"))
eng=int(input("Enter The Marks Of English"))
total= sci+maths+eng
avg= total/3
print("Roll No \t",rollno ,"Name \t ",name," Total \t",total," Avg \t",avg ,)
if(avg>=80):
    print("Grade : A")
elif(avg>=60):
    print("Grade: B")
elif(Avg>=40):
    print("Grade : C")
else:
    print("Fail....")
        
