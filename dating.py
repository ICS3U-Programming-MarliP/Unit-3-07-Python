#!usr/bin/env python3
# Created By: Marli Peters
# Date: Nov. 13, 2023
# This program asks the user if they are really good looking
# and if they are rich then if they are either of those things the user
# will be given permission to date my grandchild.

def main():
    # introduction statement
    print("Can you date my grandchild? Find out by answering these questions.")
    print("")

    # get user looks and wealth
    looks_str = str(
        input("Are you really good looking? Answer with 1 for yes or 2 for no: ")
    )
    rich_str = str(input("Are you rich? Answer with 1 for yes or 2 for no: "))
    print("")

    # change user input from string to int
    try:
        looks_int = int(looks_str)
        rich_int = int(rich_str)

    # catch input errors
    except:
        print("Please answer with 1 or 2.")

    else:
        # give user response based on input
        if looks_int == 1 or rich_int == 1:
            print("You may date my grandchild.")

        elif looks_int == 2 and rich_int == 2:
            print("You may not date my grandchild.")

        # catch other errors
        else:
            print("Please answer with 1 or 2.")


if __name__ == "__main__":
    main()
