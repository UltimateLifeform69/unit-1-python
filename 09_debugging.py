#Problem 1
text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":
       #Made a space in the if statement to count the amount of spaces in a sentence.
       count += 1

print(count)

#Problem 2
print("give me a number")
#The input is seen as a string 
n = int(input())
#variable was n and every other variable is num
for num in range(1, n):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")


num = int(input("Enter an integer: "))

if num < -1:
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num):
    result *= i   

  print("Factorial of " + num + "is" + result)