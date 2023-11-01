import statistics
from collections import Counter
numbers = [16,18,27,16,23,21,19]
mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)
def calculate_mode(arr):
    counter = Counter(arr)
    max_count = max(counter.values())
    mode = [num for num, count in counter.items() if count == max_count]
    return mode
custom_mode = calculate_mode(numbers)

print("Mean:", mean)
print("Median:", median)
print("Mode (using statistics library):", mode)
print("Mode (using custom function):", custom_mode)



