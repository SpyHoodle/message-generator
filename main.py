import pyfiglet
import colour as c
import json
import random
import time
import sys
import os


def pretty_print(text, colour, wait):
    print(colour, end="")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(wait)
    print(c.end)


def open_data(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data


def get_from_input(code, data):
    output = []
    for i in range(len(code)):
        output.append(data[i][code[i]])
    return " ".join(output)


def get_from_random(data):
    generated = []
    for i in range(0, len(data)):
        number = random.choice(data[i])
        generated.append(number)
    return " ".join(generated)


def ask_another():
    inp = input(f"{c.cyan}Create another?{c.end} {c.blue}(Y/n){c.end}: ")

    if inp.lower() == "n":
        return True

    else:
        return False


def print_output(output):
    os.system("clear")
    pretty_print(pyfiglet.figlet_format(output), c.magenta, 0.002)
    pretty_print(output, c.green, 0.02)


def main(file):
    os.system("clear")

    print(f"{c.magenta}Potentially Random Message Generator (PRMG) v1.1{c.end}")
    choice = input(f"{c.cyan}(R){c.end}{c.blue}andom Generation,{c.end} {c.cyan}(I){c.end}{c.blue}nput yourself,{c.end} {c.red}(Q){c.end}{c.blue}uit{c.end}\n{c.green}> {c.end}").upper()

    if choice == "R" or choice == "RANDOM":
        stop = False
        while stop is False:
            data = open_data(file)
            output = get_from_random(data)
            print_output(output)

            stop = ask_another()

        main(file)

    elif choice == "I" or choice == "INPUT":
        stop = False
        while stop is False:
            data = open_data(file)
            code = []

            for group in data:
                os.system("clear")
                print(f"{c.cyan}Options:{c.end}")

                count = 0
                for phrase in group:
                    print(f"{c.magenta}{count}:{c.end} {c.blue}{phrase}{c.end}")
                    count += 1

                valid = False
                while valid is False:
                    number = input(f"{c.cyan}Input a number from the list: {c.end}")

                    if number.isnumeric() is False:
                        print(f"{c.red}Error: Choice is not numeric{c.end}\n")

                    elif int(number) >= len(group) or int(number) < 0:
                        print(f"{c.red}Error: Out of list range{c.end}\n")

                    else:
                        code.append(int(number))
                        valid = True

            output = get_from_input(code, data)
            print_output(output)

            stop = ask_another()

        main(file)

    elif choice == "Q" or choice == "QUIT":
        print(f"{c.red}Goodbye! Exiting...{c.end}")

    else:
        print(f"{c.red}Error: Not a valid option from the menu{c.end}")

        time.sleep(0.5)
        main(file)


if __name__ == "__main__":
    main("peptalk.json")
