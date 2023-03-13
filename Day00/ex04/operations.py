#!/usr/bin/env python3
from sys import argv

def main():
    """@description: This program is a calculator.
    @params: number A, number B
    """
    errors = {
        "usage": "Usage: python3 operations.py <integer A != 0> <integer B > 0>\nExample:\n\tpython3 operations.py 10 3",
        "too_many_arguments": "InputError: too many arguments.",
        "too_few_arguments": "InputError: not enough arguments.",
        "divider_by_zero": "ERROR: (division by 0)",
        "module_by_zero": "ERROR: (modulo by 0)"
    }
    if (len(argv) > 3):
        return print(errors["too_many_arguments"])
    elif (len(argv) < 3):
        return print(errors["too_few_arguments"])
    sum = int(argv[1]) + int(argv[2])
    diff = int(argv[1]) - int(argv[2])
    prod = int(argv[1]) * int(argv[2])
    quot = (int(argv[2]) == 0) and errors["divider_by_zero"] or int(argv[1]) / int(argv[2])
    rem = (int(argv[2]) == 0) and errors["module_by_zero"] or int(argv[1]) % int(argv[2])
    print("Sum: {sum}\nDifference: {diff}\nProduct: {prod}\nQuotient: {quot}\nRemainder: {rem}".format(sum=sum, diff=diff, prod=prod, quot=quot, rem=rem))    
    return
    
if(__name__ == '__main__'):
    main()