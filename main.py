# A series of simple algorithms


# Maximum of three numbers:
def max(a, b, c):
    max = 0
    nums = [a, b, c]
    for num in nums:
        if num > max:
            max = num
    print(max)


# Checking if number is prime:
def prime(numar):
    count = 0
    for i in range(1, numar + 1):
        if numar % i == 0:
            count += 1
    if count == 2:
        print("Este numar prim")
    else:
        print("nu este prim")


# Printing the Fibonacci sequence:
def fibonacci(limita):
    n_1 = 0
    n_2 = 1
    print(n_1)
    print(n_2)
    for i in range(0, limita):
        sum = n_1 + n_2
        print(sum)
        n_1 = n_2
        n_2 = sum


# Largest number in a list:
def max_list(numbers):
    max = 0
    for number in numbers:
        if number > max:
            max = number
    print(max)


# Smallest number in a list:
def min_list(numbers):
    min = 99999999
    for number in numbers:
        if number < min:
            min = number
    print(min)


# Sum of the digits of a number:
def sum_digits(n):
    sum = 0
    string = str(n)
    for i in string:
        sum += int(i)
    print(sum)


# Check if number is palindrome:
def palindrome(n):
    count = 0
    reverse = str(n)[::-1]
    for i in range(0, len(str(n))):
        if str(n)[i] == reverse[i]:
            count += 1
    if count == len(str(n)):
        print("Este palindrom")
    else:
        print("Nu este palindrom")


# Sum of the first n natural numbers:
suma = 0


def sum_n(n):
    global suma
    if n > 0:
        suma = suma + n
        sum_n(n - 1)
    return suma


# Find the sum of the digits of a number until it is a single digit:
def sum_last_digit(n):
    text = str(n)
    result = 0
    for i in range(len(text) - 1):
        result += int(text[i])
    print(result)


# Find the sum of the squares of the first n natural numbers:
def squares_of_n(n):
    result = 0
    for i in range(1, n + 2):
        result = result + i ** 2
    print(result)


max(14, 9, 13)
prime(7)
fibonacci(5)
max_list([14, 9, 3])
min_list([14, 2, 3])
sum_digits(334)
palindrome(344)
print(sum_n(3))
sum_last_digit(2347)
squares_of_n(4)
