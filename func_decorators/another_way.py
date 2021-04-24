# functions are first class objects in python & we can simulate the same behaviour of decorator with that
import time


def calculate_execution_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print("Total Time Taken : ", time.time()-start)

    return inner


def calculate_mean(num_list):
    time.sleep(3)
    return len(num_list)/2


decorated = calculate_execution_time(calculate_mean)
nums = [1, 5, 8, 7, 66, 22]
decorated(nums)