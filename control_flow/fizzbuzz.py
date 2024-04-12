x = 0
while x < 100:
    x += 1
    y = x % 3
    z = x % 5
    w = x % 15
    if w is 0:
        print("FizzBuzz")
    elif z is 0:
        print("Buzz")
    elif y is 0:
        print("Fizz")
    else:
        print(x)