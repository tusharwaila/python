#take two number as input from user ,take the operation he need to perform and print the result
## by apke apne debugger bhaiya

a = int(input("enter 1 number: "))
b = int(input("enter 2 number: "))
operation = input("ENTER THE TYPE OF OPERATION YOU WANT TO PERFORM(+,-,*,/): ")
if operation == '+':
   result = a+b
elif operation == '-':
     result = a-b
elif operation == '*':
     result = a*b
elif operation == '/':
     result = a/b
else: 
	result = "INVALID OPERATION"
print("THE RESULT IS :",result)
