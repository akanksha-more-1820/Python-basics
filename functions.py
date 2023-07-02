# tom_exp = [100, 200, 300]
# john_exp = [400, 500, 600]

# total=0
# for item in tom_exp:
#     total=total+item
# print("toms total exp",total)
#
# total=0
# for item in john_exp:
#     total=total+item
# print("johns total exp",total)

# using functions
# def calculate_total(exp,name):
#     total=0
#     for items in exp:
#         total = total + items
#     print(name," total is:-",total)
#
# toms_total = calculate_total(tom_exp,"tom")
# johns_total=calculate_total(john_exp,"John")

# print(johns_total)
# print(toms_total)

total=0
def sum(a,b=0):

    """

   This document
    """
    print(a)
    print(b)
    total=a+b
    print(total)

sum(5)



