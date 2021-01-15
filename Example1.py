"""
Example 1.
"""
n = 5
m = 1
k = 4
size_of_object = [4, 2, 3, 4, 1]
# The output will be 1

index = n-1
counter_of_object = 0
sum_of_sizes = 0

for box in range(m):
    sum_of_sizes = size_of_object[n-counter_of_object-1]
    while sum_of_sizes <= k:
        sum_of_sizes = sum_of_sizes + size_of_object[index-1]
        counter_of_object = counter_of_object + 1
        index = index - 1

if __name__ == '__main__':
    print("---------------------------------------------")
    print("The maximum number of objects in the boxes is: ", counter_of_object)
#   print("j=", index + 2)
