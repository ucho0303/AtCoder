import glob
import os

flist = glob.glob('./A?C/???/*.py')
flist.sort()
for f in flist:
    os.rename(f,f[:10] + f[13:])