def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


marks = [80, 90, 70, 60]

result = calculate_average(marks)

print("Average:", result)
