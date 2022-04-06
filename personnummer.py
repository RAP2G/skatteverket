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
            print(con_sum)
        if con_sum % 10 == 0:
            return True
        else:
            return False

    def print_ID(self, *err: str):
        print(f"{self.year+self.month+self.day+self.number}     {err}")

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_number(self):
        return self.number


def create_ID_object(id_number: str):
    id_number = id_number.strip()
    id = IdNumber(id_number[:2], id_number[2:4],
                  id_number[4:6], id_number[6:])
    return id


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
            if inp.isdecimal():
                if len(inp) == 10:
                    id = create_ID_object(inp)
                    if id.valid_date() != True:
                        id.print_ID("Invalid date")
                    elif id.checksum() != True:
                        id.print_ID("Incorrect checksum")
                    else:
                        id.print_ID()
                elif len(inp) > 10:
                    print(f"{inp}   Too long")
                else:
                    print(f"{inp}   Too short")

            else:
                print(f"{inp}   Doesn't only contain numbers")
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
