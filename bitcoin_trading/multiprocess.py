import multiprocessing as mp
import time

def worker():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    time.sleep(5)
    print("SubProcess End")


# 'This program is being run by itself'

###메인함수가 실행될때만 실행되도록 만약에 import하는경우는 실행안되게 하는것
if __name__ == "__main__":
    #main process
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)

    #process spawning
    p = mp.Process(name="SubProcess", target=worker)
    p.start()


    print("MainProcess End")