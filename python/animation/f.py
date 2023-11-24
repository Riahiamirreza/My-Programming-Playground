import time


for i in range(47):
    for j in range(178):
      print("\033[{};{}H".format(i,j)+"f",end="")
