import threading
import time

class Ex_1:
    def __init__(self, threads):
        self.threads = threads
        self.semaphore = threading.Semaphore(threads)
        self.thread_pool = []
    
    def complete_tasks(self, task_id):
        with self.semaphore:
            print(f"Задача {task_id} запущена")
            time.sleep(1)  
            print(f"Задача {task_id} завершена")
    
    def set_time(self, num_tasks):
        start_time = time.time()

        for task_num in range(1, num_tasks + 1):
            thread = threading.Thread(target=self.complete_tasks, args=(task_num,))
            thread.start()
            self.thread_pool.append(thread)

        for thread in self.thread_pool:
            thread.join()
        
        end_time = time.time()
        self._print_performance_report(start_time, end_time, num_tasks)
    
    def _print_performance_report(self, start_time, end_time, num_tasks):

        total_time = end_time - start_time
        print(f"Общее время выполнения: {total_time:.2f} секунд")