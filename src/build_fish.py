#!/usr/bin/env python

from time import time
start = time()

print("[BUILD] build_fish.py")

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

# render the nml file
import render_nml
render_nml.main()

# render the lang files
import render_lang
render_lang.main()

# render the docs

import render_docs
render_docs.main()


print((time() - start))
