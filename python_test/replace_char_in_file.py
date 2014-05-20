import sys
import os

def doFileWork(filename):
    ext = os.path.splitext(filename)[-1]
#    if ext != ".py": return
    f = open(filename)
    before = f.read()
    f.close()
    after = before.replace("ABC", "DEF")
    f = open(filename, "w")
    f.write(after)
    f.close()

doFileWork(sys.argv[1])
