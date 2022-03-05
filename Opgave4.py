import time

#Del 1
def part1():
    amount = int(input("Hvor mange tal vil du lægge sammen? "))
    numbers = []
    for x in range(amount):
        numbers.append(int(input("Skriv et tal: ")))
    operator = input("Vælg en operator: ")
    equation = ""
    for index, num in enumerate(numbers):
        if (index + 1) != len(numbers):
            equation += str(num) + operator
        else:
            equation += str(num)
    print("Udregnet: ", eval(equation))

#Del 2
def part2():
    words = ['hej', 'test', 'bla', 'python', 'bla', 'hej', 'bla']
    amounts = {}
    for word in words:
        if word not in amounts:
            amounts[word] = 0
        amounts[word] += 1
    print(amounts)

#Del Shakespeare
def shakeSpeare():
    start = time.time()

