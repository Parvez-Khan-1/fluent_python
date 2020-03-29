def maturity(age):
    return age > 18


ages = [18, 16, 15, 21, 16, 24, 25, 26, 27]

filtered_ages = list(filter(maturity, ages))
print("Matured Ages : ", filtered_ages)