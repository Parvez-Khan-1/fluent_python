import time


def calculate_execution_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print("Total Time Taken : ", time.time()-start)

    return inner


@calculate_execution_time
def calculate_mean(num_list):
    time.sleep(3)
    return len(num_list)/2


nums = [10, 12, 5, 3, 8, 9, 44, 66, 22, 35, 37]
calculate_mean(nums)