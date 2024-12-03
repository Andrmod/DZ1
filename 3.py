from random import randint
n = int(input("Введіть ваше число: "))
a = randint(1, 10)
while n != a:
  if n > a:
    print("Ваше число більше за загадане")
    n = int(input("Введіть ваше число щераз: "))
  else:
    print("Ваше число менше за загадане")
  n = int(input("Введіть ваше число щераз: "))
if n ==a:
  print("Ви вгадали!")