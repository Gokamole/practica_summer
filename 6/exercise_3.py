import asyncio

class Ex_3:
    def __init__(self, initial_value=0, num_coroutines=4, iterations=3):
        self.variable = initial_value
        self.lock = asyncio.Lock()
        self.num_coroutines = num_coroutines
        self.iterations = iterations
    
    async def modify_variable(self, coroutine_name):
        for i in range(self.iterations):
            await asyncio.sleep(1)  
            
            async with self.lock:
                self.variable += 1
                print(f"{coroutine_name}: {self.variable}")
    
    async def run_coroutines(self):
        tasks = []        
        for i in range(self.num_coroutines):
            coroutine_name = f"Корутина {i+1}"
            tasks.append(self.modify_variable(coroutine_name))        
        await asyncio.gather(*tasks)
    
    def get_final_value(self):
        return self.variable
    
async def main():
        manager = Ex_3(initial_value=0, num_coroutines=4, iterations=3)
        await manager.run_coroutines()

def Ex3():
    asyncio.run(main())