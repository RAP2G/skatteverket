from msilib.schema import File
from os import listdir, name, system
from os.path import isfile, join, exists
from datetime import date, datetime


class IdNumber:
    def __init__(self, year, month, day, number) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.number = number

    def valid_date(self):
        is_valid_date = True
        try:
            datetime(int(self.year), int(self.month), int(self.day))
        except ValueError:
            is_valid_date = False
        return is_valid_date

    def checksum(self):
        con_sum = 0
        id_number = self.year+self.month+self.day+self.number
        for i in range(len(id_number)):
            if i % 2 == 0:
                prod = int(id_number[i])*2
                if len(str(prod)) > 1:
                    for x in str(prod):
                        con_sum += int(x)
                else:
                    con_sum += prod
            else:
                con_sum += int(id_number[i])
        if con_sum % 10 == 0:
            return True
        else:
            return False

    def print_ID(self, err: str = ""):
        print(f"{self.year+self.month+self.day+self.number}     {err}")

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_number(self):
        return self.number

    def get_ID(self):
        return self.year+self.month+self.day+self.number


def clearConsole(): return system('cls' if name in ('nt', 'dos') else 'clear')


def validate_format(inp: str):
    if "-" == inp[6]:
        return True
    elif "-" == inp[7] and "-" == inp[4] and " " == inp[10]:
        return True
    elif " " == inp[2] and " " == inp[5] and " " == inp[8]:
        return True
    elif len(inp) == 10 and inp.isdecimal():
        return True
    else:
        return False


def convert_input_to_standrad_format(inp: str):
    """
    Format of inp must be validated with the function validate_format() before inserting into this function
    """
    if "-" == inp[6]:
        return inp.replace("-", "")
    elif "-" == inp[7] and "-" == inp[4] and " " == inp[10]:
        return inp.replace("-", "").replace(" ", "")[2:]
    elif " " == inp[2] and " " == inp[5] and " " == inp[8]:
        return inp.replace(" ", "")
    else:
        return inp


def create_ID_object(id_number: str):
    id_number = id_number.strip()
    id = IdNumber(id_number[:2], id_number[2:4],
                  id_number[4:6], id_number[6:])
    return id


def write_invalid(inp: str, err, invalids: list):
    file_exists = exists("ValidatedInputs/InvalidIDs.txt")
    if file_exists:
        for i in invalids:
            if inp in i:
                return
    with open("ValidatedInputs/InvalidIDs.txt", "a") as f:
        f.write(f"{inp}     {err}\n")


def validate_ID_number(inp: str, valids: list, invalids: list, file: str = "UserInputs.txt", allinputs: list = []):
    err = ""
    if len(inp) > 7:
        if validate_format(inp):
            standrad_inp = convert_input_to_standrad_format(inp)
            if len(standrad_inp) == 10:
                if standrad_inp.isdecimal():
                    id = create_ID_object(standrad_inp)
                    if id.valid_date() != True:
                        id.print_ID("Invalid date")
                        err = "Invalid date"
                        write_invalid(inp, err, invalids)
                    elif id.checksum() != True:
                        id.print_ID("Incorrect checksum")
                        err = "Incorrect checksum"
                        write_invalid(inp, err, invalids)
                    else:
                        id.print_ID()
                        for i in valids:
                            if convert_input_to_standrad_format(i) == id.get_ID():
                                break
                        else:
                            with open("ValidatedInputs/ValidIDs.txt", "a") as f:
                                f.write(f"{inp}\n")

                else:
                    print(f"{standrad_inp}    Contains non-numeric characters")
                    err = "Contains non-numeric characters"
                    write_invalid(inp, err, invalids)

            elif len(standrad_inp) > 10:
                print(f"{standrad_inp}   Too long")
                err = "Too long"
                write_invalid(inp, err, invalids)

            else:
                print(f"{standrad_inp}   Too short")
                err = "Too short"
                write_invalid(inp, err, invalids)

        else:
            print(f"{inp}   Invalid format")
            err = "Invalid format"
            write_invalid(inp, err, invalids)
    else:
        print(f"{inp}   Too short")
        err = "Too short"
        write_invalid(inp, err, invalids)
    for i in allinputs:
        if inp in i:
            return
    with open(f"ValidatedInputs/{file}", "a") as f:
        f.write(f"{inp}     {err}\n")


def read_ID_num_from_file(valids: list, invalids: list, allinputs: list):
    onlyfiles = [f for f in listdir(
        "InputsToRead") if isfile(join("InputsToRead", f))]
    print("Which file would you like to read from?")
    print("     ", end="")
    for i in range(len(onlyfiles)):
        print(f"({i+1}){onlyfiles[i]}     ", end="")
    print(f"     ({len(onlyfiles)+1})Exit")
    inp = int(input("Ans: "))
    if inp == len(onlyfiles)+1:
        return
    with open(f"InputsToRead/{onlyfiles[inp-1]}", "r") as f:
        for i in f:
            validate_ID_number(i.strip(), valids, invalids,
                               "AllValidatedtextInputs.txt", allinputs)
    input()
    clearConsole()


def read_validated_ID():
    onlyfiles = [f for f in listdir(
        "ValidatedInputs") if isfile(join("ValidatedInputs", f))]
    print("Which file would you like to read from?")
    print("     ", end="")
    for i in range(len(onlyfiles)):
        print(f"({i+1}){onlyfiles[i]}    ", end="")
    print(f"     ({len(onlyfiles)+1})Exit")
    inp = int(input("Ans: "))
    if inp == len(onlyfiles)+1:
        return
    with open(f"ValidatedInputs/{onlyfiles[inp-1]}", "r") as f:
        for i in f:
            print(i.strip())
    input()
    clearConsole()


def user_input(inp: str, valids: list, invalids: list):
    print("Please input an ID number")
    inp = input("Ans: ")
    validate_ID_number(inp, valids, invalids)
    clearConsole()


def main():
    valids = []
    invalids = []
    allinputs = []
    while True:
        file_exists = exists("ValidatedInputs/ValidIDs.txt")
        if file_exists:
            with open("ValidatedInputs/ValidIDs.txt", "r") as f:
                for i in f:
                    valids.append(i.strip())
        file_exists = exists("ValidatedInputs/InvalidIDs.txt")
        if file_exists:
            with open("ValidatedInputs/InvalidIDs.txt", "r") as f:
                for i in f:
                    invalids.append(i.strip())
        file_exists = exists("ValidatedInputs/AllValidatedTextInputs.txt")
        if file_exists:
            with open("ValidatedInputs/AllValidatedTextInputs.txt", "r") as f:
                for i in f:
                    allinputs.append(i.strip())

        inp = input("""Would you like to:
            (1)Input an ID number       (2)Read ID number for validation       (3)Read validated ID numbers       (4)Stop the programme
Ans: """)
        if inp == "1":
            clearConsole()
            user_input()

        elif inp == "2":
            clearConsole()
            read_ID_num_from_file(valids, invalids, allinputs)
        elif inp == "3":
            clearConsole()
            read_validated_ID()
        elif inp == "4":
            clearConsole()
            print("Good bye!")
            break
        else:
            print("You need to answer with either 1, 2 or 3")


if __name__ == "__main__":
    main()


# TODO: How many numbers in pnr?
# Any dash?
