#!/usr/bin/env python3

kata = (19, 9, 25, 3, 30)

def main():
    year, month, day, hour, minute = kata
    if (len(str(year)) > 4):
        print("ERROR: Year is not 4 digits")
    
    print("{month:>02}/{day:>02}/{year} {hour:>02}:{minute:>02}".format(
        month = str(month),
        day = str(day),
        year = year,
        hour = str(hour),
        minute = str(minute),
    ))
    return
    
if(__name__ == '__main__'):
    main()