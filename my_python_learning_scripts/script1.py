"""Write in a file the numbers from the given path."""


def get_numbers(lists):
    """Return list of only the numbers from list."""
    numbers = []
    for element in lists:
        if isinstance(element, (int, float)):
            numbers.append(element)
        if isinstance(element, str):
            if only_numbers(element):
                numbers.append(int(element))
            else:
                try:
                    numbers.append(float(element))
                except ValueError:
                    pass
    return numbers


def only_numbers(line):
    """Return True if line is int."""
    for element in line:
        if element not in "0123456789":
            return False
    return True


def parse_file(path):
    """Write in out.txt the numbers from the file from the given path."""
    out = open("out.txt", "w")
    with open(path) as txt:
        # gets numbers and writes them in out.txt file
        lines = txt.read().splitlines()
        line = get_numbers(lines)
        for item in line:
            out.write("%s\n" % item)
        out.close()


def main():
    """Give path to the file."""
    # write numbers in out.txt file
    path = input("Please write the path to file: ")
    parse_file(path)


if __name__ == "__main__":
    main()
