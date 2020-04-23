from queue import Queue
import  datetime
from os import listdir, chdir, getcwd


songPusher = Queue()
MY_WORKING_DIR = None
<<<<<<< HEAD

myEndtime = datetime.datetime(2020, 7, 20, 0, 0).timestamp()
#myStarttime = datetime.datetime(2020, 5, 15, 0, 0).timestamp()

def check_my_dir(dir):
    if dir in listdir():
        pass
    else:
        return None

def set_current_directory():
    global MY_WORKING_DIR

    MY_WORKING_DIR = getcwd()

    return MY_WORKING_DIR


=======

myEndtime = datetime.datetime(2020, 5, 15, 0, 0).timestamp()
myStarttime = datetime.datetime(2020, 5, 1, 0, 0).timestamp()

def check_my_dir(dir):
    if dir in listdir():
        pass
    else:
        return None

def set_current_directory():
    global MY_WORKING_DIR

    MY_WORKING_DIR = getcwd()

    return MY_WORKING_DIR


>>>>>>> master
def parser_db(res):
    pass
# def return_directory():
#     global MY_WORKING_DIR
#
#     return MY_WORKING_DIR
