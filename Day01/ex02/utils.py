colors = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "orange": "\033[34m",
    "purple": "\033[0;95m",
    "blue": "\033[36m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m",
}

def test(name:str, test, error: str, success:str):
    print("\n\n{blue}Testing: {yellow}{name}{reset}".format(name=name, yellow=colors["yellow"], reset=colors["reset"], blue=colors["blue"]))
    try:
        print("{blue}Instancing class and perfoming operations....{reset}".format(blue=colors["cyan"], reset=colors["reset"]))
        instance = test()
        print("{blue}Class Type: {green}{type}{reset}".format(
            type=type(instance),
            blue=colors["cyan"],
            green=colors["green"],
            reset=colors["reset"]
        ))
        print("{blue}Printing Instance:{reset}\n\n{instance}\n".format(instance=str(instance), blue=colors["cyan"], reset=colors["reset"]))
        print(colors["reset"])
        print(colors["cyan"] + "RESULT: " + success + colors["reset"])
    except Exception as err:
        print(colors["cyan"] + "Original Error: " + colors["orange"] + str(err) + colors["reset"])
        print(colors["cyan"] + "Entering Except: " + "RESULT: " + error + colors["reset"])
