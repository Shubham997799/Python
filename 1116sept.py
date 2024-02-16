#Accept roll no, name, marks of sci,math& eng.calculate total marks & avg of marks. print the grade
#(if avg >=80 then grade = A,avg >=60 then grade = B, avg>=40 then grade=c,& if less than 40 then fail..)
rollno=int(input("Enter Roll Number"))
name=input("Enter Name")
sci=int(input("Enter Marks of Science"))
math=int(input("Enter Marks of Maths"))
eng=int(input("Enter Marks of English"))
total= sci+math+eng
avg= total/3
print("Roll No\t,Name\t,Total\t,Avg")
print(rollno,"\t",name,"\t",total,"\t", avg)
if(avg>=80):
    print("Grade = A ")
elif(avg>=60):
    print("Grade = B")
elif(avg>=40):
    print("Grade = C")
else:
    print("Fail....")


            
