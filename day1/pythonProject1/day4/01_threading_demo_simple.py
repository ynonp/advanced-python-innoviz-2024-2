from threading import Thread
import _thread as thread

def go():
    for i in range(10):
        print("Hi! I'm thread {id} counting {i}\n".format(
            id=thread.get_ident(),
            i=i), end='')

threads = []

for _ in range(4):
    t = Thread(target=go)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

