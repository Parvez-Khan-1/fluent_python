def sqr(num):
    return num*num


numbers = [15, 16, 20, 22, 25, 26]

squared_numbers = list(map(sqr, numbers))

print("Squared Numbers : ", squared_numbers)

