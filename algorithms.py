# A series of simple algorithms


# Maximum of three numbers:
def max(a, b, c):
    max = -999999
    nums = [a, b, c]
    for number in nums:
        if number < max:
            raise ValueError("Numbers should not be less than -999999")
    for num in nums:
        if num > max:
            max = num
    return max


# Checking if number is prime:
def prime(numar):
    count = 0
    if numar < 0:
        raise ValueError("number should be positive")
    for i in range(1, numar + 1):
        if numar % i == 0:
            count += 1
    if count == 2:
        print("prime")
        return "prime"
    else:
        print("not prime")
        return "not prime"


# Printing the Fibonacci sequence:
def fibonacci(limita):
    if limita == 0:
        return 0
    elif limita == 1:
        return [0, 1]
    else:
        n_1 = 0
        n_2 = 1
        result = []
        result.append(n_1)
        result.append(n_2)
        for i in range(0, limita - 2):
            sum = n_1 + n_2
            result.append(sum)
            n_1 = n_2
            n_2 = sum
        return result


# Largest number in a list:
def max_list(numbers):
    max = -999999
    for number in numbers:
        if number < max:
            raise ValueError("Numbers should not be less than -999999")
    for number in numbers:
        if number > max:
            max = number
    print(max)
    return max


# Smallest number in a list:
def min_list(numbers):
    min = 99999999
    for number in numbers:
        if number > min:
            raise ValueError("Number shouldn't be greater than 9999999")

    for number in numbers:
        if number < min:
            min = number
    print(min)
    return min


# Sum of the digits of a number:
def sum_digits(n):
    sum = 0
    string = str(n)
    if "-" in string:
        string = string.replace("-", "")
    for i in string:
        sum += int(i)
    if n > 0:
        print(sum)
        return sum
    else:
        return sum * -1


# Check if number is palindrome:
def palindrome(n):
    count = 0
    reverse = str(n)[::-1]
    for i in range(0, len(str(n))):
        if str(n)[i] == reverse[i]:
            count += 1
    if count == len(str(n)):
        return "palindrome"
    else:
        return "not palindrome"





# Find the sum of the digits of a number until it is a single digit:
def sum_last_digit(n):
    text = str(n)
    result = 0
    for i in range(len(text) - 1):
        result += int(text[i])
    return result

# Find the sum of the squares of the first n natural numbers:
def squares_of_n(n):
    result = 0
    for i in range(1, n + 2):
        result = result + i ** 2
    print(result)


print(max(-14, -99, -13))
prime(73)
print(fibonacci(5))
max_list([1, 2, 3])
min_list([14, 2, 3])
print(sum_digits(123))
palindrome(344)
print(sum_last_digit(2347))
squares_of_n(4)
