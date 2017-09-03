import sys
import os

if len(sys.argv)>1:
    s = "from distutils.core import setup" + "\n" + "from Cython.Build import cythonize" + "\n" + "setup(ext_modules = cythonize(\""+str(sys.argv[1])+"\",language=\"c++\"))"
    outfile = open("setup.py","w")
    outfile.truncate(0)
    outfile.seek(0,0)
    outfile.write(s)
    outfile.close()
    exit()

if sys.version_info.major==3:
    os.system("python3 setup.py build_ext --inplace")
    exit()

if sys.version_info.major==2:
    os.system("python setup.py build_ext --inplace")
    exit()

raise Exception("Something went wrong")
