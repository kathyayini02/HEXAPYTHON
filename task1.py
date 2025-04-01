# Task 1: Print Pattern
for i in range(5, 0, -1):
    print('* ' * i)

# Task 2: Print Number Pattern
for i in range(5, 0, -1):
    print(*range(1, i+1))

# Task 3: Print Pyramid Pattern
for i in range(1, 6):
    print(*([1] + [2] * (i-2) + ([1] if i > 1 else [])))

# Task 4: Print Reverse Number Pattern
for i in range(5, 0, -1):
    print((str(i) + ' ') * i)

# Task 5: Print Incremental Number Pattern
num = 1
for i in range(1, 5):
    print(*[num + j for j in range(i)])
    num += i

# Task 6: Sum of Even and Odd Numbers
nums = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
even_sum = sum(n for n in nums if n % 2 == 0)
odd_sum = sum(n for n in nums if n % 2 != 0)
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")

# Task 7: Fibonacci Series
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()

# Task 8: Simple Calculator
while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        break
    x, y = map(float, input("Enter two numbers: ").split())
    if choice == 1:
        print("Result:", x + y)
    elif choice == 2:
        print("Result:", x - y)
    elif choice == 3:
        print("Result:", x * y)
    elif choice == 4:
        print("Result:", x / y if y != 0 else "Cannot divide by zero")
    else:
        print("Invalid choice")

# Task 9: Palindrome Checker
s = input("Enter a string: ").strip()
print("Palindrome" if s == s[::-1] else "Not a palindrome")
