initval = ""
compval = ""

while initval != "quit":
    print("give me a value! (or quit)")
    initval = input()
    if initval == "quit":
        break
    if initval.isdigit() == True:
        initval = int(initval)
        print("give me another number!")
        compval = int(input())
        if initval > compval:
            print(f"{initval} is greater than {compval}")
        elif initval < compval:
            print(f"{initval} is lesser than {compval}")
        elif initval == compval:
            print(f"{initval} is equal than {compval}!")
    else:
        print("give me another word!")
        compval = input()
        if len(initval) > len(compval):
            print(f"{initval} is longer than {compval}")
        elif len(initval) < len(compval):
            print(f"{initval} is shorter than {compval}")
        elif len(initval) == len(compval):
            print(f"{initval} is the same size as {compval}!")
