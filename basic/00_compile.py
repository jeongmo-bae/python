# https://www.python-course.eu/python3_formatted_output.php
import  py_compile
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print('os.getcwd : ' + os.getcwd())
py_compile.compile(__file__)
print(os.listdir('./__pycache__'))  # ['00_compile.cpython-311.pyc']

