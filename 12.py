users_age_groups = {
    "Андрій": "Дорослий",
    "Марія": "Молода",
    "Олексій": "Підліток",
    "Олена": "Дитина"
}

user_name = input("Введіть ім'я користувача: ")


if user_name in users_age_groups:
    print(f"{user_name} належить до вікової групи: {users_age_groups[user_name]}")
else:
    print(f"Ім'я {user_name} не знайдено у словнику.")