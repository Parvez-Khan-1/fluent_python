# Using Local Variable


def averager():
    count = 0
    sum = 0

    def average(num):
        nonlocal count, sum
        count += 1
        sum += num
        return sum/count
    return average


avg = averager()
print(avg(10))
print(avg(15))
print(avg(20))