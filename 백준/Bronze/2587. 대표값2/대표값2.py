number = [None for _ in range(5)]
for i in range(5):
    number[i] = int(input())
average = sum(number) // len(number)
number.sort()
median = number[2]
print(average)
print(median)