import time

a = [
    "[          ]",
    "[>         ]",
    "[<>        ]",
    "[<<>       ]",
    "[<<<>      ]",
    "[<<<<>     ]",
    "[<<<<<>    ]",
    "[<<<<<<>   ]",
    "[<<<<<<<>  ]",
    "[<<<<<<<<> ]",
    "[<<<<<<<<<>]",
    "[ <<<<<<<<>]",
    "[  <<<<<<<>]",
    "[   <<<<<<>]",
    "[    <<<<<>]",
    "[     <<<<>]",
    "[      <<<>]",
    "[       <<>]",
    "[        <>]",
    "[         >]"
        ]

b = ["\\","|","/","-"]

for i in range(10000):
    print("\033[s",end="")
    print("\033[1; 165H"+a[(i+1)%len(a)],end="\r")
    print("\033[2; 165H"+a[(i+2)%len(a)],end="\r")
    print("\033[3; 165H"+a[(i+3)%len(a)],end="\r")
    print("\033[4; 165H"+a[(i+4)%len(a)],end="\r")
    print("\033[5; 165H"+a[(i+5)%len(a)],end="\r")
    print("\033[6; 165H"+a[(i+6)%len(a)],end="\r")
    print("\033[7; 165H"+a[(i+7)%len(a)],end="\r")
    print("\033[8; 165H"+a[(i+8)%len(a)],end="\r")
    print("\033[9; 165H"+a[(i+9)%len(a)],end="\r")
    print("\033[10;165H"+a[(i+10)%len(a)],end="\r")
    print("\033[11;165H"+a[(i+11)%len(a)],end="\r")
    print("\033[12;165H"+a[(i+12)%len(a)],end="\r")
    print("\033[13;165H"+a[(i+13)%len(a)],end="\r")
    print("\033[14;165H"+a[(i+14)%len(a)],end="\r")
    print("\033[15;165H"+a[(i+15)%len(a)],end="\r")
    print("\033[16;165H"+a[(i+16)%len(a)],end="\r")
    print("\033[17;165H"+a[(i+17)%len(a)],end="\r")
    print("\033[18;165H"+a[(i+18)%len(a)],end="\r")
    print("\033[19;165H"+a[(i+19)%len(a)],end="\r")
    print("\033[20;165H"+a[(i+20)%len(a)],end="\r")
    print("\033[21;165H"+a[(i+21)%len(a)],end="\r")
    print("\033[22;165H"+a[(i+22)%len(a)],end="\r")
    print("\033[23;165H"+a[(i+23)%len(a)],end="\r")
    print("\033[24;165H"+a[(i+24)%len(a)],end="\r")
    print("\033[25;165H"+a[(i+25)%len(a)],end="\r")
    print("\033[26;165H"+a[(i+26)%len(a)],end="\r")
    print("\033[27;165H"+a[(i+27)%len(a)],end="\r")
    print("\033[28;165H"+a[(i+28)%len(a)],end="\r")
    print("\033[29;165H"+a[(i+29)%len(a)],end="\r")
    print("\033[30;165H"+a[(i+30)%len(a)],end="\r")
    print("\033[31;165H"+a[(i+31)%len(a)],end="\r")
    print("\033[32;165H"+a[(i+32)%len(a)],end="\r")
    print("\033[33;165H"+a[(i+33)%len(a)],end="\r")
    print("\033[34;165H"+a[(i+34)%len(a)],end="\r")
    print("\033[u", end="")
    time.sleep(.1)
