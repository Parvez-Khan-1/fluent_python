# Continues average with nested function


def averager():
    series = []

    def average(new_value):
        series.append(new_value)  # We are able to append it because lists are mutable
        total = sum(series)
        return total/len(series)

    return average

avg = averager()
print(avg(10))
print(avg(15))
print(avg(20))