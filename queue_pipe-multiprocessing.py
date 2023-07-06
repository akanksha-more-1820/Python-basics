import time
import multiprocessing

#using shared memory for accessing global variables in main and child process

square_res=[]
def calc_square(numbers):
    global square_res
    print("calculate square numbers")
    for number in numbers:
        # time.sleep(5)
        print('square:-',number*number)
        square_res.append(number*number)
        print("within process result:-", square_res)


if __name__ =="__main__":
    arr=[2,3,8,9]
    p1=multiprocessing.Process(target=calc_square,args=(arr,))


    p1.start()


    p1.join()
    # p2.join()

    print("global res= ",square_res)
    print("done")
