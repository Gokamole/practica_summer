import time
import threading

class Ex_2:
    def __init__(self, files):
        self.files = files
        self.posled_time = 0
        self.parallel_time = 0
    
    def chtenie_files(self, filename):
        print(f"Начало обработки {filename}")
        time.sleep(10) 
        print(f"Завершение обработки {filename}")
    
    def posled(self):
        print("ПОСЛЕДОВАТЕЛЬНАЯ ОБРАБОТКА")
        
        start_time = time.time()
        
        for file in self.files:
            self.chtenie_files(file)
        
        self.posled_time = time.time() - start_time
    
    def parallel(self):
        print("ПАРАЛЛЕЛЬНАЯ ОБРАБОТКА")
        
        threads = []
        start_time = time.time()
        
        for file in self.files:
            thread = threading.Thread(target=self.chtenie_files, args=(file,))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        self.parallel_time = time.time() - start_time
    
    def results(self):
        print(f"Время последовательной обработки: {self.posled_time:.2f} секунд")
        print(f"Время параллельной обработки: {self.parallel_time:.2f} секунд")
