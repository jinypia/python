#tab2spc.py
#tap to space

import re
import sys

def usage():
    print("Usage: python %s filename [no. of space]" % sys.argv[0])

try: f = open(sys.argv[1])
except: usage(); sys.exit(2)

msg = f.read()
f.close()
p = re.compile(r'\t')
# r : raw, r'\t' => '\\t' 

changed = p.sub(" "*int(sys.argv[2]), msg)

f = open(sys.argv[1], 'w')
f.write(changed)
f.close()
