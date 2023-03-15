colors = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "orange": "\033[34m",
    "purple": "\033[0;95m",
    "blue": "\033[30m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m",
}

def test(name:str, test, error: str, success:str):
    print("\n\nTesting: " + colors["yellow"] + name + colors["reset"])
    try:
        print("Instancing class...")
        instance = test()
        print("Type: {color}{type}{reset}".format(
            type=type(instance),
            color=colors["green"],
            reset=colors["reset"]
        ))
        print("Printing Instance:\n\n{instance}\n".format(instance=str(instance)))
        print(colors["reset"])
        print(colors["green"] + "RESULT: " + success + colors["reset"])
    except Exception as err:
        print(colors["red"] + "Original Error: " + colors["orange"] + str(err) + colors["reset"])
        print(colors["red"] + "Entering Except: " + "RESULT: " + error + colors["reset"])
