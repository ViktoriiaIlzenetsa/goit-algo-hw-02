from queue import Queue
import time
import random

#Створити чергу заявок
queue = Queue()


def generate_request(queue, id):
    queue.put(id)


def process_request(queue):
    if not queue.empty():
        current_request = queue.get()
        print(f"Request {current_request} is being processed")
    else:
        print("Queue is empty")

def main():
    id = 0
    # створюємо заявки, рандомну кількість від 2 до 5
    for i in range(random.randint(2, 5)):
            time.sleep(1)
            generate_request(queue, id)
            id += 1
            print(f"Queue - {list(queue.queue)}")
    # поки черга не буде пустою кожну секунду буде або додаватись заявка або ні і оброблятись по одній заявці
    while not queue.empty():
        time.sleep(1)
        for i in range(random.randint(0, 1)):
            generate_request(queue, id)
            id += 1
        print(f"Queue - {list(queue.queue)}")
        process_request(queue)
    print("Queue is empty")
       
      
if __name__ == "__main__":
    main()
