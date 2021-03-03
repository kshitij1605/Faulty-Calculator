
# Faulty Calculator
num1=float(input("Enter First No."))
num2=float(input("Enter Second No."))
op=input("Enter operator +,-,*,/")
if num1==45 and num2==3 and op=='*':
    print("555")
elif num1==56 and num2==9 and op=='+':
    print("77")
elif  num1==56 and num2==6 and op=='/':
    print("4")
elif op=='+'  :
    print("The sum is : ",num1+num2)
elif op=='-'  :
    print("The Subtract is : ", num1 - num2)
elif op=='*' :
    print("The multiple is : ", num1 * num2)
elif op=='/':
    print("The multiple is : ", num1 / num2)
else:
    0


