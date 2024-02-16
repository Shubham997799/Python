rollno= int(input("Enter Roll Number"))
name=input("Enter Name")
sci=int(input("Enter Marks Of Science"))
math=int(input("Enter Marks Of Maths"))
eng=int(input("Enter Marks Of English"))
total= sci+maths+eng
avg= total/3
print("Roll Number /t,Name \t,Total \T,Avg",rollno"\t",name"\t",total"\t",avg)
if(avg>=40):
    print("Pass...."):
        else:
            print("Fail...")

