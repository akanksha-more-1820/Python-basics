class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def print_exception(self):
        print("user defined exception",self.msg)


def process_file():
    try:
        f=open("D:\\funny_wc.txt")
        x=1/0
    except FileNotFoundError as e:
        print("inside expect")
    finally:
        print("cleaning files")
        f.close()

    f.close()

process_file()



try:
    raise Accident ('cars crashed')
except Accident as e:
    e.print_exception()