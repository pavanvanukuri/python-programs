Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="python programing"
>>> print(a.lower())
python programing
>>> print(a.upper())
PYTHON PROGRAMING
>>> print(a.title())
Python Programing
>>> print(a.capitalize())
Python programing
>>> print(a.isdigit())
False
>>> print(a.isalpha())
False
>>> print(a.isalnum())
False
>>> print(a.index('o'))
4
>>> print(a.count('p'))
2
>>> print(a.split())
['python', 'programing']
>>> print(a.strip())
python programing
>>> python programing
SyntaxError: invalid syntax
>>> a="   python   "
>>> print(a.rstrip())
   python
>>> print(a.lstrip())
python   
