def a(x,y): 
    for i in range(x): 
        for j in range(y): 
            if random.choice([1,0]): 
                print("\033[{};7m  \033[0m".format(random.choice([i for i in range(29,39)])), end="") 
            else: 
                print("  ", end="") 
        print()

import sys
import random

a(int(sys.argv[1]), int(sys.argv[2]))

