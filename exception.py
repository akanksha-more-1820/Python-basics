x=input("enter no -1")
y=input("enter no -2")
try:
    z=x/int(y)
except ZeroDivisionError as e:
    print("division by zero exception")
    z= None
except Exception as e:
    print("Type error exception")
    z=None
print("dvision is :-",z)