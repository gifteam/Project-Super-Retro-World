from cx_Freeze import setup, Executable
import os, sys
from distutils.dir_util import copy_tree

# On appelle la fonction setup
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

target = Executable(
    script="main.py",
    base=None,
    icon="icon.ico"
    )

setup(
    name="Main",
    version="1.0",
    description="the description",
    author="the author",
    options={"build_exe": build_exe_options},
    executables=[target]
    )
s = "src"
d = "build\exe.win32-3.6\src"
copy_tree(s,d)
