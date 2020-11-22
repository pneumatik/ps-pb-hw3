# Словарь account
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}
account = [account1, account2, account3, account4]

# Словарь user_list
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}
user_list = [user1, user2, user3, user4]

# Ввод ключа
user_name = input('Введите ключ (name или account): ').lower()

try:
    print(f"значение ключа {user_name} для юзера 1 = {user1[user_name]}")
    print(f"значение ключа {user_name} для юзера 2 = {user2[user_name]}")
    print(f"значение ключа {user_name} для юзера 3 = {user3[user_name]}")
    print(f"значение ключа {user_name} для юзера 4 = {user4[user_name]}")
except:
    print('Введенный ключ не найден')

# Ввод номера юзера
user_number = int(input('Введите порядковый номер: '))
try:
    print(f"Данные по юзеру № {user_number}: \n"
          f"Имя: {user_list[user_number-1]['name']} \n"
          f"Возраст: {user_list[user_number-1]['age']} \n"
          f"Аккаунт: {account[user_number-1]['login']} \n"
          f"Пароль: {account[user_number-1]['password']}")
except:
    print('Пользователь с указанным номером не найден')

# Средний возраст пользователей
average_age = (user1['age']+user2['age']+user3['age']+user4['age']) / len(user_list)
print('Средний возраст пользователей: ' + str(average_age))

# Перемещение пользователя
user_number_2 = int(input('Введите номер пользователя, которого нужно переместить в конец: '))
print('Список до изменения:')
print(user_list)
print('Пользователь с именем ' + user_list[user_number_2-1]['name'] + ' перемещен в конец')

new_user_list_1 = user_list.copy()
new_user_list_1.remove(user_list[user_number_2-1])

new_user_list_2 = new_user_list_1.copy()
new_user_list_2.append(user_list[user_number_2-1])

print('Список после изменения:')
print(new_user_list_2)
