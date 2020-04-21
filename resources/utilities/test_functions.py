import os, sys

def testpath():
    if getattr(sys, 'frozen', False):
        CurrentPath = sys._MEIPASS
        print('firstif', CurrentPath)
        # If it's not use the path we're on now
    else:
        CurrentPath = os.path.dirname(__file__)
        print('second if', CurrentPath)