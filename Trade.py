Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
os.getcwd()
'C:\\Python310.1'
os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python310.dll', 'pythonw.exe', 'Scripts', 'share', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']
text1 = 'เปลี่ยนแปลง+1.00'
text2 = '%เปลี่ยนแปลง+2.58%'
len('เปลี่ยนแปลง')
11
word = 'abcdefg'
print(word[:3])
abc
print(word[3:])
defg
text1 = 'เปลี่ยนแปลง+1.00'print(word[3:])
SyntaxError: invalid syntax
text1 = 'เปลี่ยนแปลง+1.00'
\
print(text1[11:])
+1.00
print(word[1:3])
bc
print(type(text1))
<class 'str'>
print(int(text1))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(int(text1))
ValueError: invalid literal for int() with base 10: 'เปลี่ยนแปลง+1.00'
print(type(text1[11:]))
<class 'str'>
print(int(text1[11:]))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(int(text1[11:]))
ValueError: invalid literal for int() with base 10: '+1.00'
int(text1[11:]))
SyntaxError: unmatched ')'
int(text1[11:])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(text1[11:])
ValueError: invalid literal for int() with base 10: '+1.00'
len('เปลี่ยนแปลง')
11
print(text2[12:])
+2.58%
print(text2[12:-1])
+2.58
float(text2[12:-1])
2.58
(float(text2[12:-1])/100) * 200
5.16
float(text2[12:-1]) * 100
258.0
