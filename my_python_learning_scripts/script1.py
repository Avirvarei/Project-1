def get_numbers(list):
    numbers = []
    for element in list:
        if type(element) == int or type(element) == float:
            numbers.append(element)
        if type(element) == str:
            if only_numbers(element):
                numbers.append(int(element))
            else:
                try:
                    numbers.append(float(element))
                except ValueError:
                    pass
    return numbers


def only_numbers(line):
    # returns True or False after checking if element is integer
    for element in line:
        if element not in "0123456789":
            return False
    return True


def parse_file(path):
    out = open("out.txt", "w")
    with open(path) as file:
        # gets numbers and writes them in out.txt file
        lines = file.read().splitlines()
        line = get_numbers(lines)
        for item in line:
            out.write("%s\n" % item)
        out.close()


def main():
    # writes numbers in out.txt file
    path = input("Please write the path to file: ")
    parse_file(path)


if __name__ == "__main__":
    # execute only if run as a script
    main()
