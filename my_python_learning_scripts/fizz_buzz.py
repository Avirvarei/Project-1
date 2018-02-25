def fizz_buzz(number):
    list = []
    for i in range(1, number + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            list.append("FizzBuzz")
        elif (i % 3 == 0):
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(str(i))
    return ",".join(list)


def main():
    while True:
        n = input("Please write a natural number: ")
        # check if input is not number
        if n == "exit":
            exit(0)
        try:
            print(fizz_buzz(int(n)))
        except ValueError:
            print("This is not a natural number!")


if __name__ == "__main__":
    main()
