path = 'C:/Users/dorof/PycharmProjects/pythonProject1/testingtypes.txt'
test_file = open(path, 'r')
test_file.readlines()
title = 'Types of the Non-functional Testing\n'
path = 'C:/Users/dorof/PycharmProjects/pythonProject1/testingtypes.txt'
test_file = open(path,'r')
types = test_file.read()
new_path = 'C:/Users/dorof/PycharmProjects/pythonProject1/nonfunc_testingtypes.txt'
nonfunc_testingtypes = open(new_path,'w')
nonfunc_testingtypes.write(title)
print(title)
nonfunc_testingtypes.write(types)
print(types)

test_file.close()
nonfunc_testingtypes.close()
import os
b = os.path.getsize("C:/Users/dorof/PycharmProjects/pythonProject1/testingtypes.txt")
c = os.path.getsize("C:/Users/dorof/PycharmProjects/pythonProject1/nonfunc_testingtypes.txt")
print(b)
print(c)