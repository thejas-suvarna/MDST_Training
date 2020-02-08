"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    # num = int(input("Enter a number"))
    if (num % 2 == 0):
        print("even")
    else:
        print("odd")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """

    while(True):
        random.seed()
        num = random.randint(1, 9)
        guess = input("What is your guess?")
        if(guess == "exit"):
            return
        elif(int(guess) > num):
            print("Too High")
        elif (int(guess) < num):
            print("Too Low")
        else:
            print("Correct!")



def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    left = 0
    right = len(string) - 1

    while(left <= right):
        if string[left] != string[right]:
            print("Not a palindrome")
            return
        left += 1
        right -= 1

    print("Is a palindrome")


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """


    with open(filename, "wb") as file:
        file.writelines([base64.b64encode(username.encode("ascii")), bytes("\n".encode("ascii")), base64.b64encode(password.encode("ascii"))])

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    username = None
    with open(filename, "rb") as file:
        username = base64.b64decode(file.readline())
        passw = base64.b64decode(file.readline())
        print("Username:", username.decode("ascii"))
        print("Password:", passw.decode("ascii"))

    if password != None:
        with open(filename, "wb") as file:
            file.write(base64.b64encode(username))
            file.write(bytes("\n".encode("ascii")))
            file.write(base64.b64encode(password.encode("ascii")))


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
