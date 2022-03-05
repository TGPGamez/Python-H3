#Del 1
def part1():
    print("Del 1")
    x = 17
    y = 12.0
    z = "4"

    print(type(x))
    print(type(y))
    print(type(z))

    print(2 * x)
    print(x / 2.0)
    print(x + y)
    print(1 + 2 * 3)
    print(z * 4)

#Del 2
def part2():
    print("Del 2")
    x = 1
    y = 2 # + 3
    # x = 5
    z = x + y
    print(z)
    #Printer 3

#Del 3
def part3():
    print("Del 3")
    x = int(input("Skriv første tal: "))
    y = int(input("Skriv andet tal: "))
    print("Summen: ", (x + y))

#Del 4
def part4():
    print("Del 4")
    x = float(input("Skriv første tal: "))
    y = float(input("Skriv andet tal: "))
    print("Summen: ", (x + y))

#Del 5
def part5():
    print("Del 5")
    tal = [65, 81, 43, 63, 27, 69, 43, 68, 88, 76, 30, 99, 74, 11, 89, 38, 73, 9]
    sum = 0
    highestValue = 0
    highestValuePos = 0;
    for index, num in enumerate(tal):
        sum += num;
        if num > highestValue:
            highestValue = num
            highestValuePos = index
        if num > 40 and num < 70:
            print(num)
    print("Summen: ", sum)
    print("Højeste tal: ", highestValue)
    print(" - Position: ", highestValuePos)

#Del 6
def part6():
    amount = int(input("Hvor mange tal vil du lægge sammen? "))
    sum = 0
    for x in range(amount):
        sum += int(input("Skriv et tal: "))
    print("Summen er: ", sum)