import time
from multiprocessing import Process, Queue


def work(name, tasks_to_accomplish, tasks_that_are_done):
    while not tasks_to_accomplish.empty():
        item = tasks_to_accomplish.get_nowait()
        time.sleep(0.5)
        tasks_that_are_done.put(item)
        print(f"Task no {str(item)} is done by Process-{str(name)}")


if __name__ == '__main__':
    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()

    for i in range(10):
        tasks_to_accomplish.put(i)
        print(f"Task no {str(i)}")

    processes = [
        Process(target=work, args=(i, tasks_to_accomplish, tasks_that_are_done))
        for i in range(4)
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
