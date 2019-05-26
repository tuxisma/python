from pprint import pprint as p
import os
import glob

file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
p(file_sizes)



