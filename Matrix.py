X = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]

Y = [[5,8,1],
[6,7,3],
[4,5,9]]

result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)
result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
 print(r)

# Program to check if a string is palindrome or not

my_str = "albohPhoBiA"

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
  print("The string is a palindrome")
    