#!/usr/bin/python

from distutils.core import Extension, setup
from Cython.Build import cythonize
from sysconfig import get_paths

import glob, subprocess, sys, os

if sys.version_info.major != 3:
    sys.exit("Sorry, but this script is only for python 3")

try:
    os.remove("build")
except: pass

module = [
    {"name": "app/controllers/" , "module": glob.glob("src/controllers/*.cpp")},
    {"name": "app/lang/"        , "module": glob.glob("src/lang/*.cpp")},
    {"name": "app/module/"      , "module": glob.glob("src/module/*.cpp")},
]

extensions = []
for ext in module:
    for file in ext["module"]:
        extensions.append(Extension(name=(ext["name"]+file.split("/").pop().split(".")[0]), sources=[file]))

setup(
      name="Lumine",
      version="2.4",
      author="Unknown God",
      ext_modules=cythonize(extensions, language_level=3)
)

include = get_paths()["include"]

subprocess.check_call([
    "gcc",
    "-Os",
    "-I",
    include,
    "-o",
    "lumine",
    "src/lumine.cpp",
    "-l{py}".format(py=include.split("/").pop()),
    "-lpthread",
    "-lm",
    "-lutil",
    "-ldl"
])

try:
    if subprocess.call(["sudo", "chmod", "+x", "lumine"], stdout=subprocess.PIPE) != 0:
        raise Exception()
except:
    subprocess.call(["chmod", "+x", "lumine"], stdout=subprocess.PIPE)
finally:
    pass
