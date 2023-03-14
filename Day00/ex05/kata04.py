#!/usr/bin/env python3

kata = (0, 4, 132.42222, 10000, 12345.67)

def main():
    module, ex, a, b, c = kata
    print("module_{module:02d}, ex_{ex:02d} : {a:.2f}, {b:.2e}, {c:.2e}".format(module = module, ex = ex, a = a, b = b, c = c))
    return
    
if(__name__ == '__main__'):
    main()