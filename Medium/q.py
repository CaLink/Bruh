from typing_extensions import Concatenate


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def bold(func):
    def wrapper(*args,**kwargs):
        #func(*args,**kwargs)
        print(color.BOLD, *args)
    return wrapper

def Underline(func):
    def wrapper(*args,**kwargs):
        #func(*args,**kwargs)
        print(color.UNDERLINE, *args)
    return wrapper

def Grn(func):
    def wrapper(*args,**kwargs):
        #func(*args,**kwargs)
        print(color.GREEN, *args)        
    return wrapper

def end(func):
    def wrapper(*args,**kwargs):
        #func(*args,**kwargs)
        print(color.CYAN, *args,color.END)        
    return wrapper

