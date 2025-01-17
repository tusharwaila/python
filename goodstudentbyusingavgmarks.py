#take two students and take their name and marks for maths,physics and chemistry and compare the avg of the two students marks and display the good student
student1 = input("enter the name of the first student: ")
s1m = int(input("enter math marks of first student: "))
s1p = int(input("enter physics marks of first student: "))
s1c = int(input("enter chemistry marks of third student: "))
avg1 = (s1m+s1p+s1c)/3
print(avg1)
student2 = input("enter the name of the second student: ")
s2m = int(input("enter math marks of second student: "))
s2p = int(input("enter physics marks of second student: "))
s2c = int(input("enter chemistry marks of second student: "))
avg2 = (s2m+s2p+s2c)/3
print(avg2)
if avg1>avg2:
    print("student1 is good in studies")
else:
    print("student2 is good in studies")
