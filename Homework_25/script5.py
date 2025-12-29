print("Wellcome to calculiator")
print("Enter first digit ")
a=int(input())
print("Enter second digit ")
b=int(input())
print("Enter arithmetic operation: + - * /")
o=str(input())
if o=="+":
    print(a+b)
elif o=="-":
    print(a-b)
elif o=="*":
    print(a*b)
elif o=="/":
    print(a/b)
