#!/usr/bin/env python3

kata = (2019, 9, 25, 3, 30)

def main():
    year, month, day, hour, minute = kata
    if (len(str(year)) > 4):
        print("ERROR: Year is not 4 digits")
    
    print("{month}/{day}/{year} {hour}:{minute}".format(
        month = str(month).zfill(2),
        day = str(day).zfill(2),
        year = year,
        hour = str(hour).zfill(2),
        minute = str(minute).zfill(2)
    ))
    return
    
if(__name__ == '__main__'):
    main()