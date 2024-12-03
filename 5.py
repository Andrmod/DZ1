n = int(input("Введіть число n: "))
for n in range(n, 0, -1):
    if n % 2 == 0:
        print(n, end=" ")