from os import listdir, name, system
from os.path import isfile, join
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

    def print_ID(self, **err: str):
        print(f"{self.year+self.month+self.day+self.number}     {err}")

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_number(self):
        return self.number


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


def validate_ID_number(inp):
    if validate_format():
        standrad_inp = convert_input_to_standrad_format(inp)
        if len(standrad_inp) == 10:
            if standrad_inp.isdecimal():
                id = create_ID_object(standrad_inp)
                if id.valid_date() != True:
                    id.print_ID("Invalid date")
                elif id.checksum() != True:
                    id.print_ID("Incorrect checksum")
                else:
                    id.print_ID()

            else:
                print(f"{inp}    Contain non-numeric characters")
        elif len(inp) > 10:
            print(f"{inp}   Too long")
        else:
            print(f"{inp}   Too short")
    else:
        print(f"{inp}   Invalid format")
        print(""" 
        Valid formats:
            620129-8558
            62 01 29 8558
            1962-01-29 8558
            6201298558
        
        """)


def read_ID_num_from_file():
    print("File read function will be here")


def clearConsole(): return system('cls' if name in ('nt', 'dos') else 'clear')


def main():
    while True:
        inp = input("""Would you like to:
            (1)Input an ID number       (2)Read ID number from a file       (3)Stop the programme
Ans: """)
        if inp == "1":
            clearConsole()
            print("Please input an ID number")
            inp = input("Ans: ")
            validate_ID_number(inp)
            print()
        elif inp == "2":
            clearConsole()
            read_ID_num_from_file()
        elif inp == "3":
            clearConsole()
            print("Good bye!")
            break
        else:
            print("You need to answer with either 1 or 2")


if __name__ == "__main__":
    main()
