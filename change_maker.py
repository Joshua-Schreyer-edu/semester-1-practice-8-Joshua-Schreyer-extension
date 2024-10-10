"""
This program takes in the total amount due and the amount that has been paid
and will output the change due, including what dollars and coins you need to give.
It also simulates a real change machine, with different balances of different coins.
Joshua Schreyer - October 2024
"""

import sys
import random
import time

def get_input(this_input):
    if this_input + 1 < len(sys.argv):
        return sys.argv[this_input+1]
    else:
        return input()

def main() -> None:
    # iniate amounts of change with random values
    num_dollars: int = random.randint(1, 10)
    num_quarters: int = random.randint(1, 8)
    num_dimes: int = random.randint(1, 10)
    num_nickels: int = random.randint(1, 20)
    num_pennies: int = random.randint(1, 50)


    # get inputs
    amount_due: float = float(get_input(0))
    amount_paid: float = float(get_input(1))

    # get change due
    change_due: float = amount_paid - amount_due

    # because computers do that
    # silly thing with floats
    change_due = round(change_due, 2)

    # print change due
    change_due_string = str(change_due)
    if len(change_due_string) < 4:
        change_due_string += "0"
    print(f"Change Due: ${change_due_string}")

    # get dollars
    dollars = int(change_due // 1)
    if dollars <= num_dollars:
        print(f"Dollar Bills: {dollars}")
        change_due = change_due - dollars
        num_dollars = num_dollars - dollars
    else:
        change_due = change_due - num_dollars
        print(f"Dollar Bills: {num_dollars}")
        num_dollars = 0
        print("""
        Oops, we don't have enough dollars!
        Using next form of change to compensate...
        """)

    #get quarters
    quarters = int(change_due // 0.25)
    if quarters <= num_quarters:
        print(f"Quarters: {quarters}")
        change_due = change_due - (quarters * 0.25)
        num_quarters = num_quarters - quarters
    else:
        change_due = change_due - (num_quarters * 0.25)
        print(f"Quarters: {num_quarters}")
        num_quarters = 0
        print("""
        Oops, we don't have enough quarters!
        Using next form of change to compensate...
        """)

    #get dimes
    dimes = int(change_due // 0.1)
    if dimes <= num_dimes:
        print(f"Dimes: {dimes}")
        change_due = change_due - (dimes * 0.1)
        num_dimes = num_dimes - dimes
    else:
        change_due = change_due - (num_dimes * 0.1)
        print(f"Dimes: {num_dimes}")
        num_dimes = 0
        print("""
        Oops, we don't have enough dimes!
        Using next form of change to compensate...
        """)

    # because computers do that
    # silly thing with floats
    change_due = round(change_due, 2)

    # get nickels
    nickels = int(change_due // 0.05)
    if nickels <= num_nickels:
        print(f"Nickels: {nickels}")
        change_due = change_due - (nickels * 0.05)
        num_nickels = num_nickels - nickels
    else:
        change_due = change_due - (num_nickels * 0.05)
        print(f"Nickels: {num_nickels}")
        num_nickels = 0
        print("""
        Oops, we don't have enough nickels!
        Using next form of change to compensate...
        """)

    # because computers do that
    # silly thing with floats
    change_due = round(change_due, 2)

    # get pennies
    pennies = int(round((change_due / 0.01),2))
    if pennies <= num_pennies:
        print(f"Pennies: {pennies}")
        change_due = change_due - (pennies * 0.01)
    else:
        change_due = change_due - (num_pennies * 0.01)
        print(f"Pennies: {num_pennies}")
        num_dimes = 0
        print("""
        Oops, we don't have enough pennies!
        Looks like you ain't getting your money back :b
        """)
        time.sleep(3.5)
        print("""
        Just kidding! Please proceed
        to a staff member for assistance.
              """)


if __name__ == "__main__":
    main()