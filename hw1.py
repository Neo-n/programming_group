# Print out a pyramid of stars N in this pattern
# *
# * *
# * * *
# * * * *
# Change the input paramater for N and print N by N *s
def problem1(N):
    return None


# Function to take in user input and return (a) Addition, (s) Subtraction, (m) Multiplication, or (d) Division of 2 numbers
# IE:
# > First Number? 4
# > Second Number? 6
# > Operation ((a) Addition, (s) Subtraction, (m) Multiplication, or (d) Division)? m
# > Result: 24
def problem2():
    return None

# Swap the variables given to you so the value of b is in a and the value of a is in b
def problem3(a, b):
    return a, b


# Implement this encription algorithm
# https://learncryptography.com/classical-encryption/caesar-cipher
def problem4():
    return None


def run():
    while True:
        print("Which problem do you want to run? \n(1) problem1\n(2) problem2\n(3) problem3\n(4) problem4\n(q) QUIT")
        choice = input()

        if '1' in choice:
            n = int(input("What do you want for N? "))
            print(problem1(n))
        elif '2' in choice:
            print(problem2())
        elif '3' in choice:
            a = input("Input a: ")
            b = input("Input b: ")
            print(problem3(a, b))
        elif '4' in choice:
            print(problem4())
        else:
            break

run()