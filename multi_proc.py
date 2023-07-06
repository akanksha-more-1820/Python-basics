import time
import multiprocessing

square_res=[]
def calc_square(numbers):
    global square_res
    print("calculate square numbers")
    for number in numbers:
        # time.sleep(5)
        print('square:-',number*number)
        square_res.append(number*number)
        print("within process result:-", square_res)

# def calc_cube(numbers):
#     print("calculate cube numbers")
#     for number in numbers:
#         time.sleep(5)
#         print('cube:-', number * number*number)


if __name__ =="__main__":
    arr=[2,3,8,9]
    p1=multiprocessing.Process(target=calc_square,args=(arr,))
    # p2= multiprocessing.Process(target=calc_cube, args=(arr,))


    p1.start()
    # p2.start()

    p1.join()
    # p2.join()

    print("global res= ",square_res)
    print("done")
