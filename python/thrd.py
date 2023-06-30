import timeit
import time
import threading


TARGET = int(1e6)

def countdown(n):
    if n <= 0: return
    while n:
        n -= 1

def run_multi(n):

    threads = [
        threading.Thread(target=countdown, args=(TARGET,)) for i in range(n)
    ]

    for t in threads: t.start()
    for t in threads: t.join()


result = timeit.timeit(stmt=lambda: countdown(TARGET), number=20)
print(result)

result = timeit.timeit(stmt=lambda: run_multi(3), number=20)
print(result)
