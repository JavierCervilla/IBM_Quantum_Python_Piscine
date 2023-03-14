#!/usr/bin/env python3
import sys
from time import sleep
from datetime import datetime

""" 
def func():
    for i in range(0,11):
        if (i == 0):
            y = 0
        y += i
        yield y
        
for x in func():
    print(x) 
"""

def ft_proggress(list):
    initial_timestamp = datetime.now()
    step = 0
    for elem in list:
        step += 1
        yield step
        last_timestamp = datetime.now()
        percent = (step / len(list)) * 100
        eta = ((last_timestamp - initial_timestamp).total_seconds() / step) * (len(list) - step)
        color = "\033[1;32;40m"
        reset = "\033[0;37;40m"
        loading_bar = "{}".format(int(percent / 5) * "█")
        elapsed_time = (last_timestamp - initial_timestamp).total_seconds()
        sys.stdout.write('\r')
        bar = "ETA: {eta:.2f}s [{percent:>2.0f}%][{color}{loading_bar:<20}{reset}] {steps}/{total} | elapsed time {elapsed_time:.2f}s".format(
            eta=eta,
            percent=percent,
            loading_bar=loading_bar,
            steps=step,
            total=len(list),
            elapsed_time=elapsed_time,
            color=color,
            reset=reset
        )
        sys.stdout.write(bar)
        sys.stdout.flush()


def main():
    list = range(1000)
    ret = 0
    for elem in ft_proggress(list):
        ret += (elem + 3) % 5
        sleep(0.005)
    print()
    print(ret)
    
if(__name__ == '__main__'):
    main()
    
    
