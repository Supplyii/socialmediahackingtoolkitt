import os
from multiprocessing import Process
import sys
try:
    port = sys.argv[1]
except Exception:
    port = ""
def script1():
    os.system("python3 file1.py "+port)     
def script2():
    os.system("python3 file2.py") 

if __name__ == '__main__':
    p = Process(target=script1)
    q = Process(target=script2)
    p.start()
    q.start()
    p.join()
    q.join()
    