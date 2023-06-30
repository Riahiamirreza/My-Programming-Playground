import time

def show(string="test" ,delay=0.2 , time_=5):

    sh = [i+"  "+string+"  "+i for i in ["\\","|","/","-"]]
    for i in range(time_):
        print(sh[i%4], end="\r")
        time.sleep(delay)

show("hello",0.1,20)
