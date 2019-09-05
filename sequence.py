n = int(input("Enter the length of the sequence: ")) # Do not change this line
first = 3
second = 2
third = 1

for i in range(n):
    if i <= 2:
        print(i+1)
    else:
        print(first + second + third)
        temp_1 = first
        temp_2 = second
        temp_3 = third
        first = temp_1 + temp_2 + temp_3
        second = temp_1
        third = temp_2
    i += 1