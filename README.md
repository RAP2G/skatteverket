# Skatteverket

## Language and Libraries

This program uses Python 3.10.1 adn its os and datetime libraries.

## Before Running The Program

Before you can run the program you need to check if the following conditions are met:

- There should be two folders called InputsToValidate and ValidatedInputs

- Inside ValidatedInputs there should be four files called:

  - AllValidatedInputs.txt
  - InvalidIDs.txt
  - UserInputs.txt
  - ValidIDs.txt

After all this the program should be runnable

>**Additional Information**
>
> Any files that you would want to read from for validation should be put inside the folder InputsToValidate.
>ID numbers inside the input file should also be written according to the following format:
>
>         yymmdd-xxxx
>         yy mm dd xxxx
>         yyyy-mm-dd xxxx
>         yymmddxxxx
>

## Guide To Using The Program

To run the program input the following into the terminal:

```cmd
    py personnummer.py
```

**You need to be inside the root directory of the project for this to work!**

After running the code it reads the content of the files inside "ValidatedInputs" and assigns their values to lists which then are used to prevent duplicate ID numbers from being saved onto them. This should take no time at all so the menu should show up immediately.  

In the menu you are prompted to choose between four options:

1. Input an ID number
2. Read ID number for validation
3. Read validated ID numbers
4. Stop the program

To interact with the UI you should **always** write the numbers infron of the options as inputs

## License

[MIT](https://choosealicense.com/licenses/mit/)
