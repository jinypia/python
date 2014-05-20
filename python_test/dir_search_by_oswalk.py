import os
import sys

for (path, dir, files) in os.walk(sys.argv[1]):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))
