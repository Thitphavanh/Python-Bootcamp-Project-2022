# checkfile.py
import os

path = os.getcwd()
print(path)
allfile = os.listdir(path)
print(allfile)

print('Apples.jpg' in allfile)

print(os.path.join(path, 'Apples.jpg'))