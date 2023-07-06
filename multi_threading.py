import time
import  threading



def calc_square(numbers):
    print("calculate square numbers")
    for number in numbers:
        time.sleep(0.2)
        print('square:-',number*number)


def calc_cube(numbers):
    print("calculate cube numbers")
    for number in numbers:
        time.sleep(0.2)
        print('cube:-', number * number*number)
start=time.time()
array=[2,3,4,5]
t1=threading.Thread(target=calc_square,args=(array,))
t2=threading.Thread(target=calc_cube,args=(array,))

t1.start()
t2.start()
t1.join()
t2.join()
end=time.time()

print("took second:- "+ str(end-start))