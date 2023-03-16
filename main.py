import sys
from interface import *

if __name__ == '__main__':
    #reset the log files
    with open('rubiklog.txt','w') as s:
        s.writelines('')
    with open('solution.txt','w') as s:
        s.writelines('')
    menu()