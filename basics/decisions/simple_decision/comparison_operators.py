print("Please enter the first number")
first = int(input())

print("Please enter the second number")
second = int(input())

if (first < second):
  print("{} is smaller than {}".format(first, second))
elif (second < first):
  print("{} is smaller than {}".format(second, first))
else:
  print("both numbers are equal")