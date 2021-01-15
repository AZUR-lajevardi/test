"""
Main program.
This program was written by Dr. Mohammadreza Lajevardi and his team from Kashan Islamic Azad University.
The name of the team is "Azure".
hoshmandcomputer@gmail.com

n is the number of objects. m is the number of boxes. k is the maximum size of boxes.

You must input n, m, k and the size of n objects (Enter what you want).
"""
n = int(input("Input number of objects (n): "))
m = int(input("Input number of boxes (m): "))
k = int(input("Input size of boxes(k): "))

size_of_object = []

for i in range(n):
    size_of_object.append(int(input("Input size of object (Less than or equal to k): ")))
    if size_of_object[i] > k:
        while size_of_object[i] > k:
            print("You made a mistake")
            del size_of_object[-1]
            size_of_object.append(int(input("Input size of object (Less than or equal to k): ")))

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
#   print("index=", index + 2)
#   exit()
