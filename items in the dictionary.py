"""
 The program takes a dictionary and prints the sum of all the items in the dictionary.
Problem Solution:
1. Declare and initialize the n number of dictionary values from the user.
2. Find the sum of all the values in the dictionary.
3. Print the total sum.
4. Exit.
Sample Input:
3
100
540
239
"""
n = int(input("Enter the number of items in the dictionary: "))
my_dict = {}
for i in range(n):
    key = input(f"Enter key for item {i + 1}: ")
    value = int(input(f"Enter value for item {i + 1}: "))
    my_dict[key] = value
total_sum = sum(my_dict.values())
print("Total sum of values in the dictionary:", total_sum)
