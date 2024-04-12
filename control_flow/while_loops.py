x = 0


while x < 10:
    print(f"x -> {x}")
    x += 1
    if x > 4:
        break

# Without declaring x the code doesn't work. If I didn't include "x += 1" the code would run forever.