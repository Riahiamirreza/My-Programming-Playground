import time

a = [i for i in range(100)]

for i in a:
    print("%"+str(i),end="\r")
    time.sleep(0.1)
