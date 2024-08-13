from concurrent.futures import ThreadPoolExecutor
import time

def function1():
    for i in range(5):
        print(f"Function 1 - iteration {i}")
        time.sleep(1)

def function2():
    for i in range(5):
        print(f"Function 2 - iteration {i}")
        time.sleep(1)

# Create a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as executor:
    # Submit functions to the executor
    future1 = executor.submit(function1)
    future2 = executor.submit(function2)

# Both functions will run concurrently
print("Both functions have been submitted to the executor.")
