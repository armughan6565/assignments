print("   MARKSHEET OF SSC_I        ")
name_of_student=input("enter your name")
roll_no=input("enter your roll no")
no_of_subject=input("enter no of subject")
feild=input("enter your feild")         
english_marks=int(input("please enter english marks"))
sindhi_marks=int(input("please enter sindhi marks"))
pst_marks=int(input("please enter pst marks"))
chemistry_marks=int(input("please enter chemistry marks"))
computer_marks=int(input("please enter computer marks"))
if chemistry_marks<0 or chemistry_marks>100:
     print("invalid chemistry_input")
if sindhi_marks<0 or sindhi_marks>75:
     print("invalid sindhi_input")
if pst_marks<0 or pst_marks>75:
     print("invalid pst_marks")
if english_marks<0 or english_marks>100:
     print("invalid english_marks")
if computer_marks<0 or computer_marks>100:
     print("invalid computer_marks")
print(name_of_student)
print(roll_no)
print(feild)     
x=computer_marks+chemistry_marks+sindhi_marks+pst_marks+english_marks
y=(x / 425*100)
print(y)
if  y>80:
     print("     CONGRATULATION YOU GOT A-ONE GRADE ")
if y<79 or y>40:
     print("     YOU ARE PASSED")
if y<39:
     print("   YOU ARE FAILED ")
