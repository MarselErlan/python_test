import os
say1 = open("test.txt", "r")
a = (f"say {say1.read()}")
print(a)
os.system(a)
say1.close()
