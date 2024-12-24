def check_age(age):
    try:
        assert age >= 18, "Вам має бути 18 років або більше щоб використовувати цей сервіс"
        print("Ви можете використовувати цей сервіс")
    except AssertionError as e:
        print(e)

check_age(20)
check_age(16)