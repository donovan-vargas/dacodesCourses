def square_walk(t):
    for x in range(0, t):
        n = int(input("rows: "))
        m = int(input("columns: "))
        if n > m:
            if m % 2 == 0:
                print("U")
            else:
                print("D")
        else:
            if n % 2 == 0:
                print("L")
            else:
                print("R")


square_walk(4)
