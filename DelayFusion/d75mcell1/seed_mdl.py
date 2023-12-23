#!/usr/bin/env python

import os, sys

nu = input('which seed do you want to run? :')
number = int(nu)
i = number

os.system("mcell -seed %i d4.mdl" % (i,))
os.system("mcell -seed %i d5.mdl" % (i,))
os.system("mcell -seed %i d75.mdl" % (i,))
os.system("mcell -seed %i 1d.mdl" % (i,))
os.system("mcell -seed %i 1d5.mdl" % (i,))
os.system("mcell -seed %i 2d.mdl" % (i,))
os.system("mcell -seed %i 2d5.mdl" % (i,))
os.system("mcell -seed %i 3d.mdl" % (i,))
os.system("mcell -seed %i 3d5.mdl" % (i,))
os.system("mcell -seed %i 4d.mdl" % (i,))
os.system("mcell -seed %i 5d.mdl" % (i,))
os.system("mcell -seed %i 6d.mdl" % (i,))
os.system("mcell -seed %i 7d.mdl" % (i,))
os.system("mcell -seed %i 8d.mdl" % (i,))
os.system("mcell -seed %i 10d.mdl" % (i,))
os.system("mcell -seed %i 12d.mdl" % (i,))
os.system("mcell -seed %i 15d.mdl" % (i,))
os.system("mcell -seed %i 20d.mdl" % (i,))
os.system("mcell -seed %i Full.mdl" % (i,))
