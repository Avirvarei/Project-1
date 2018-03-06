"""Return fizzbuzz list until the number from input."""
from __future__ import print_function


def fizz_buzz(number):
    """Return a list containing fizzbuzz list."""
    lists = []
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            lists.append("FizzBuzz")
        elif i % 3 == 0:
            lists.append("Fizz")
        elif i % 5 == 0:
            lists.append("Buzz")
        else:
            lists.append(str(i))
    return ",".join(lists)


def main():
    """Give a natural number to print the fizzbuzz list."""
    while True:
        user_input = input("Please write a natural number: ")
        # check if input is not number
        if user_input == "exit":
            exit(0)
        try:
            print(fizz_buzz(int(user_input)))
        except ValueError:
            print("This is not a natural number!")


if __name__ == "__main__":
    main()
