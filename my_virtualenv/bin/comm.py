#!/home/shane/Desktop/Projects/Biof_395/my_virtualenv/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from biorun.methods.comm import run
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(run())
