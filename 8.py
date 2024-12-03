a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
o = input("Введіть операцію (+, -, *, /): ")
if o == "+":
    r = a + b
elif o == "-":
    r = a - b
elif o == "*":
    r = a * b
elif o == "/":
    if b == 0:
        r = "Ділення на нуль"
    else:
        r = a / b
else:
    r = "Невідома операція"
print(f"Результат: {r}")