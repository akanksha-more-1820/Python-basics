# num=input("enter a number :- ")
# num=int(num)
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")

# //cuisine menu

indian=["samosa","daal","naan"]
chinese=["eggroll","noodles","fried rice"]
italian=["pizza","pasta","rissotto"]

dish=input("enter a dish name:- ")
if dish in indian:
    print("Indian dish")
elif dish in chinese:
    print("Chinese dish")
elif dish in italian:
    print("Italian dish")
else:
    print("other dish")

