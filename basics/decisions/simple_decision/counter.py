print("Please enter first number")
first = int(input())

print("Please enter second number")
second = int(input())

print("Please enter third number")
third = int(input())

num_even = 0
num_odd = 0

if (first % 2 == 0):
  num_even += 1
else:
  num_odd += 1

if (second % 2 == 0):
  num_even += 1
else:
  num_odd += 1

if (third % 2 == 0):
  num_even += 1
else:
  num_odd += 1

print("There were {} even and {} odd numbers.".format(num_even, num_odd))