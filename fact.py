def fact(number):
    end = 1
    for i in range(1, number + 1):
        end *= i
    print(end)


fact(1000)
