#Del 1
def part1():
    _input = input("Skriv en sætning: ").replace(" ", "")
    backwards = _input[::-1]
    if _input == backwards:
        print("Sætningen er et palindrom")
    else:
        print("Sætningen er ikke et palindrom")