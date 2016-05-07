# This file compiles the main latex document (which needs to be updated to reflec the main .tex file) and then cleans the garbage output by running cleanDirectory.py

import os
from cleanDirectory import cleanDirectory

os.system("python sample_chart.py")
os.system("latexmk -pdf Math_Notes.tex")
cleanDirectory()
