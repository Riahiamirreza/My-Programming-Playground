import time
animation = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]

a = [i for i in range(100)]

i = 0

for i in a:
    print(animation[i % len(animation)]+"-[%"+str(i)+"]", end='\r')
    time.sleep(.1)


