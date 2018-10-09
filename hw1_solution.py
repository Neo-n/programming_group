# Welcome to your first programming challenge!
# Below, we have given you four puzzles to solve, in increasing difficulty. 
# Do as many as you can (we believe in you)! 

# Should you run into any scary bugs or dead ends, we have compiled a small programmers survival guide for you. 
# It goes as follows:

# 1) Google whatever error message you're getting
# 2) Try and figure out better keywords to google it with
# 3) Reach out to us (contact info below)

# If you want feedback on the code you have written, you can send it to us by Sunday at 3pm the latest.
# If you send it to us any time before then we will look it over and get back to you as soon as possible.

# Good luck!

# PLEASE NOTE:
# If you are using Python Version 2.7.5 or lower, you won't be able to run this code.
# While you are able to make some changes to the code in order to fix these inconsistencies, 
# we highly recommend you download Python version 3.x.x instead (whatever the latest version of python is).
# Python 2.7 is being phased out within the next few years, so it is worthwhile getting used to the newest version now.
#
# You can download the latest version here: 
# https://www.python.org/downloads/
#
# Should you have any problems doing so, please reach out to us at rutgerscognitivescienceclub@gmail.com, or on Slack (@Yoni, or @Ranga)



# You run a software company that builds high scale pyramids for wealthy pharoahs.
# In a few weeks you will be presenting to a new client, but the client doesn't know what size pyramid he wants.
# You need to win this contract, so you really want to impress the client. Consequently, you have decided to build a demo that will
# let the Pharoah enter how many stories high he wants his pyramid. 
#
# The program you write will print out a pyramid of stars N stories high.
# ie; N = 4:
# *
# * *
# * * *
# * * * *
# 
# If you are lost and don't know where to start, try googling "loops in python"

def problem1(N):
    for num in range(1, N+1):
        for _ in range(num):
            print('*', end=' ')
        print('\n')
    return None


# Your friends don't believe you know how to code.
# Prove them wrong by solving the ultimate coding challenge: building a calculator.
# No one will deny how cool you have become should you succeed in this task.
# For now it will be a simple calculator, just to show them how terribly mistaken they were to question your programming integrity.
#
# Your calculator will take in user input and return (a) Addition, (s) Subtraction, (m) Multiplication, or (d) Division of 2 numbers
# IE:
# > First Number? 4
# > Second Number? 6
# > Operation ((a) Addition, (s) Subtraction, (m) Multiplication, or (d) Division)? m
# > Result: 24
def problem2():
    num1 = int(input("First Number? "))
    num2 = int(input("Second Number? "))
    op = input("(a) Addition, (s) Subtraction, (m) Multiplication, or (d) Division? ")
    print("Result:", end=" ")
    
    if op is 'a':
        print(num1+num2)
    elif op is 's':
        print(num1-num2)
    elif op is 'm':
        print(num1*num2)
    elif op is 'd':
        print(num1/num2)
    
    return None

# Kevin from sales has a penchant for messing things up. Every week sales improve he's supposed to send you a report on how they improved. 
# The report always has two variables: A & B. The variable A is supposed to be the lower sales number, and B is supposed to be the higher one.
# He's gotten them mixed up at least four times now, and last time it nearly cost you your job. 
# 
# With your newfound knowledge of C O M P U T E R   S C I E N C E, write a program to do the following:
#
# 1) Check if A is greater than B
# 2) If it is, swap the two numbers around, because your idiot coworker messed up again.
# 3) If A is equal to or less than B, you don't need to do anything
# 4) Return the (maybe new) values of A and B 

# ie; A = 5, B = 3,
# output: A = 3, B = 5

def problem3(A, B):
    if A < B:
        return B, A
    return A, B


# Implement this encription algorithm
# https://learncryptography.com/classical-encryption/caesar-cipher
# This function takes in the plain text which we must do a left shift on by the key's value
# NOTE: You do not need to maintain case on the output (I recomend keeping it as either lower or upper case!)
def problem4(plain_text, key):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cypher_text = []
    plain_text = plain_text.lower()
    
    for char in plain_text:
        if char == ' ':
            cypher_text.append(' ')
            continue
        ind = alphabet.index(char)
        cypher_text.append(alphabet[(ind-key)%26])

    return ("".join(cypher_text)).upper()


def run():
    while True:
        print("Which problem do you want to run? \n(1) * Pyramid\n(2) Basic Calculator\n(3) Variable Ordering\n(4) Caesar Cipher Encryption\n(q) QUIT\n")
        choice = input("Enter your choice: ")

        if '1' in choice:
            n = int(input("How many stories high would you like your pyramid? "))
            problem1(n)
        elif '2' in choice:
            problem2()
        elif '3' in choice:
            a = int(input("Input a: "))
            b = int(input("Input b: "))
            new_a, new_b = problem3(a, b)
            print("A and B have been Correctly Ordered: {new_a}, {new_b}".format(new_a=new_a, new_b=new_b))
        elif '4' in choice:
            pText = input("What do you want to encode with the Caesar Cipher? ")
            key = int(input("What key do you want to shift by? "))
            print(problem4(pText, key).upper())
        else:
            break

run()
