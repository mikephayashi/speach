some_array = []
for i in range(10):
    some_array.append(i)
    
mid = 5
before = some_array[mid - 10:mid]
after = some_array[mid: mid + 10]
print(before)
print(after)